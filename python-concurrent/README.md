# Introduction
This project is for demonstrating various concurrent techniques in Python. These techniques include `single thread`, `multiple threads`, `multiple processes`, and 
`coruntine`. 

These techniques are evaluated on two kinds of computer work, i.e. IO-bound tasks and CPU-bound tasks. It is shown here that different 
concurrent techniques can have different performance for either of these two tasks. 

Besides, for a specifical technique, different settings can 
also lead to different performance.

Overall, with this project, we can know which technique is best suitable for whick kind of tasks, and how we can configure a do configurations to make the 
most out of a particular technique.

# Usage and Result
Run this command to evaluate various concurrent techniques performance again CPU-bound/IO-bound tasks.
```shell
python compare.py repeat_num group_size step_size
```
Here, `repeat_num` means number of repeatedly run times, `group_size` means group size, and `step_size` means step size. For example, `python compare.py 5 10 10`  means repeatedly run 5 times for each size from [10, 10, ..., 10*10]. For a particular size, do an IO-bound task or CPU-bound task at this size's scale. Performance results are averaged over repeated times.
### Comparison against CPU-bound task.
![CPU-bound-task](./result/compare_cpu_bound.png)
### Comparison against IO-bound task.
![IO-bound-task](./result/compare_io_bound.png)
