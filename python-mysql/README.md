# 多线程Python程序MYSQL连接管理研究

## 研究背景
针对多用户/高并发访问mysql数据的场景，研究不同并发模式(单线程/多线程)和不同连接模式(单连接/多连接/连接池)时的程序执行效率。

## 研究手段
### 脚本
- 初始化mysql数据库
  - [init_db.py](./src/init_db.py): 包括创建DB，创建table，添加示例等。脚本只需执行一次。如果必要，请修改数据库hostname, username和password。
- 并发读取数据库内容
  - [stsc.py](./src/stsc.py): 单线程，单连接
  - [stmc.py](./src/stmc.py): 单线程，多连接
  - [mtsc.py](./src/mtsc.py): 多线程，单连接
  - [mtmc.py](./src/mtmc.py): 多线程，多连接
  - [mtcp.py](./src/mtcp.py): 多线程，连接池
### 工具
- [cProfile](https://docs.python.org/2/library/profile.html): 一种动态分析工具，测量程序每一步的执行时间。
- 使用[Linux time](https://linuxize.com/post/linux-time-command/)命令，测试程序总的执行时间。
- 使用[Limux multitime](https://tratt.net/laurie/src/multitime/)命令，测试程序在多次执行情况下的最大/平均/最小执行时间。

## 研究结果
1. 多连接的耗时显著高于单连接。
```python
root@hzettv53:~/workspace/github/python-mysql-examples# time python stsc.py
real    0m0.234s
root@hzettv53:~/workspace/github/python-mysql-examples# time python stmc.py
real    0m1.378s

```
    这是由于，MYSQL连接的创建是一件时间开销较大的操作。例如，执行命令`python -m cProfile -s cumtime stmc.py`，可以发现
```python
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.039    0.039    1.410    1.410 stmc.py:3(<module>)
     1000    0.005    0.000    1.345    0.001 stmc.py:7(read_user_from_db)
     1000    0.013    0.000    0.885    0.001 __init__.py:128(connect)
     1000    0.007    0.000    0.871    0.001 connection.py:53(__init__)
     1000    0.004    0.000    0.856    0.001 abstracts.py:711(connect)
```
2. MYSQL连接不是线程安全的。执行命令`python mtsc.py`，程序出现异常。
```python
Exception in thread Thread-102:
Traceback (most recent call last):
  File "/usr/lib/python2.7/threading.py", line 801, in __bootstrap_inner
......
    if buf[0] == 251:  # \xfb
IndexError: bytearray index out of range
```
3. 多线程时，使用连接池比使用多连接更加高效。
```python
root@hzettv53:~/workspace/github/python-mysql-examples# time python mtmc.py
real    0m2.347s
root@hzettv53:~/workspace/github/python-mysql-examples# time python mtcp.py
real    0m1.434s
```
## 总结
为了提高MYSQL数据库访问程序的性能：
- 在能使用单一连接的情况下，使用单一连接
- 在不能使用单一连接的情况下，使用连接池