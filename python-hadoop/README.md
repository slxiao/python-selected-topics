> This document describes how to run a URL counter program with signle-node Hadoop in Linux Mint. Given a file, each line of which representing a URL record, the URL counter program outputs statistical infomation abount the counts of URL and DNS, i.e. how many times a specific URL/DNS has been accessed. Map-reduce framework is adopted to solve the problem. The program runs on a single-node hadoop,  which is “pseudo-distributed” but provides a simple method for learning Hadoop basics. Similar guidelines can be found online, for example, [Running Hadoop on Ubuntu Linux (Single-Node Cluster)](http://www.michael-noll.com/tutorials/running-hadoop-on-ubuntu-linux-single-node-cluster/), [Apache Hadoop YARN Install Quick Start](http://www.informit.com/articles/article.aspx?p=2190194&seqNum=2). However, more or less, I met some problems while following these guidelines. This document aims to provide a more fresh and effective guide on how to run the first map-reduce program on single-node hadoop with newest stable [hadoop 2.7.3](http://www.nic.funet.fi/pub/mirrors/apache.org/hadoop/core/stable/hadoop-2.7.3.tar.gz), by taking the above URL counter as an example.

# Environment Setup

## VM
- Linux Mint 18.1 Serena(GNU/Linux 4.4.0-53-generic x86_64)
- 2 core CPU, 3G RAM

## VM Configuration
### Account
Create a specific user account `hduser` for running Hadoop.

```sh
mint@mint:~$ sudo addgroup hadoop
mint@mint:~$ sudo adduser --ingroup hadoop hduser
```

### SSH
Hadoop requires SSH access to manage its nodes. For single-node setup of Hadoop, as no remote machines are needed, we only need to configure SSH access to `localhost` for the hduser user we created.

```sh
mint@mint:~$ su - hduser
hduser@mint:~$ ssh-keygen -t rsa -P ""
hduser@ubuntu:~$ cat $HOME/.ssh/id_rsa.pub >> $HOME/.ssh/authorized_keys
hduser@ubuntu:~$ ssh localhost
```
## Java

Version 2.7 and later of Apache Hadoop requires Java 7. It is built and tested on both OpenJDK and Oracle (HotSpot)'s JDK/JRE. Install JDK is common and many guideline can be found [online](https://stackoverflow.com/questions/14788345/how-to-install-jdk-on-ubuntu-linux). Let the JDK is installed successfully, and the java environment variable `JAVA_HOME` is `/usr/lib/jvm/java-8-openjdk-amd64`.

## Hadoop Installation

```sh
mint@mint:~$ cd /usr/local
mint@mint:~$ wget http://www.nic.funet.fi/pub/mirrors/apache.org/hadoop/core/stable/hadoop-2.7.3.tar.gz
mint@mint:~$ sudo tar xzf hadoop-2.7.3.tar.gz
mint@mint:~$ sudo rm -rf hadoop-2.7.3.tar.gz
mint@mint:~$ sudo mv hadoop-2.7.3 hadoop
mint@mint:~$ sudo chown -R hduser:hadoop hadoop
```

## Hadoop Configuration

### System ENV Variable
Add the following lines to the end of the `$HOME/.bashrc` file of user `hduser`, then run `source $HOME/.bashrc` to the make the change effective.

```
export HADOOP_HOME=/usr/local/hadoop
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
export PATH=$PATH:$HADOOP_HOME/bin
```

### Hadoop ENV Variable

Open `/usr/local/hadoop/etc/hadoop/hadoop-env.sh`, and change the JAVA_HOME environment variable to `/usr/lib/jvm/java-8-openjdk-amd64`.
### Storage

Hadoop’s default configurations use `hadoop.tmp.dir` as the base temporary directory both for the local file system and HDFS. We can specify a path of our own, for example, `/app/hadoop/tmp` for the directory.

```
mint@mint:~$ sudo mkdir -p /app/hadoop/tmp
mint@mint:~$ sudo chown hduser:hadoop /app/hadoop/tmp
mint@mint:~$ sudo chmod 750 /app/hadoop/tmp
```
### Core Site
Add the following parts between `<configuration> ... </configuration>` tags in the file `/usr/local/hadoop/etc/hadoop/core-site.xml`:

```
<property>
  <name>hadoop.tmp.dir</name>
  <value>/app/hadoop/tmp</value>
</property>
<property>
  <name>fs.default.name</name>
  <value>hdfs://localhost:54310</value>
</property>
```
### Mapred Site

Run `cd /usr/local/hadoop/etc/hadoop/; cp mapred-site.xml.template mapred-site.xml` and then add the following parts between `<configuration> ... </configuration>` tags in the file `mapred-site.xml`:

```
<property>
  <name>mapreduce.framework.name</name>
  <value>yarn</value>
</property>
```
### Hdfs Site
Add the following parts between `<configuration> ... </configuration>` tags in the file `/usr/local/hadoop/etc/hadoop/hdfs-site.xml`:

```
<property>
  <name>dfs.replication</name>
  <value>1</value>
</property>
```
### Yarn Site
Add the following parts between `<configuration> ... </configuration>` tags in the file `/usr/local/hadoop/etc/hadoop/yarn-site.xml`:

```
<property>
   <name>yarn.nodemanager.aux-services</name>
   <value>mapreduce_shuffle</value>
 </property>
 <property>
   <name>yarn.nodemanager.aux-services.mapreduce.shuffle.class</name>
   <value>org.apache.hadoop.mapred.ShuffleHandler</value>
 </property>
```
### Format Filesystem
The first time setting up a Hadoop cluster we nee to format the filesystem by running the command:

```
hduser@ubuntu:~$ /usr/local/hadoop/bin/hadoop namenode -format
```
# Run URL counter Job

## Start Hadoop

```
hduser@mint /usr/local/hadoop $ sbin/start-dfs.sh
Starting namenodes on [localhost]
localhost: starting namenode, logging to /usr/local/hadoop/logs/hadoop-hduser-namenode-mint.out
localhost: starting datanode, logging to /usr/local/hadoop/logs/hadoop-hduser-datanode-mint.out
Starting secondary namenodes [0.0.0.0]
0.0.0.0: starting secondarynamenode, logging to /usr/local/hadoop/logs/hadoop-hduser-secondarynamenode-mint.out
hduser@mint /usr/local/hadoop $ sbin/start-yarn.sh
starting yarn daemons
starting resourcemanager, logging to /usr/local/hadoop/logs/yarn-hduser-resourcemanager-mint.out
localhost: starting nodemanager, logging to /usr/local/hadoop/logs/yarn-hduser-nodemanager-mint.out
```
## Check Start Status
Check process:

```
hduser@mint /usr/local/hadoop $ jps
31840 ResourceManager
31456 DataNode
31668 SecondaryNameNode
8598 JobHistoryServer
31341 NameNode
31950 NodeManager
32303 Jps
```
Check service: monitor HDFS file system by logging to `http://localhost:50070/` using browser, and monitor ResourceManager by logging to `http://localhost:8088` using browser.
## Prepare files
For the URL counter job, [url_data.txt](https://github.com/slxiao/URLCounter/blob/master/tst/url_data.txt) is the data file to be processed. Put the file under local file system `/home/hduser/url_data/`, then copy the file from the local file system to Hadoop’s HDFS.

```
# copy local file to HDFS
hduser@mint /usr/local/hadoop $ bin/hadoop fs -copyFromLocal /home/hduser/url_data /user/hduser/url_data
# check wether the copy operation is effective
hduser@mint /usr/local/hadoop $ bin/hadoop fs -ls /user/hduser/url_data
Found 1 items
-rw-r--r--   1 hduser supergroup        104 2017-07-30 18:48 /user/hduser/url_data/url_data.txt
```
For program files, `mapper.py` and `reducer.py`, leave them at the local file system, for example, under directory `/home/hduser/`. Make sure the two files has execution permission, by running `chmod +x /home/hduser/mapper.py` and `chmod +x /home/hduser/reducer.py`.
## Run Job
Now we can run the Python URL counter job on the Hadoop cluster. We leverage the **Hadoop Streaming API** for helping us passing data between the `mapper.py` and the `reducer.py` via STDIN and STDOUT.

```
hduser@mint /usr/local/hadoop $ bin/hadoop jar ./share/hadoop/tools/lib/hadoop-streaming-2.8.1.jar -file\
/home/hduser/mapper.py    -mapper 'python /home/hduser/mapper.py' -file\
/home/hduser/reducer.py   -reducer 'python /home/hduser/reducer.py' \
-input /user/hduser/url_data/* -output /user/hduser/url_data_output
```
## Check Job Results

```
hduser@mint /usr/local/hadoop $ bin/hadoop fs -ls /user/hduser/url_data_output
Found 2 items
-rw-r--r--   1 hduser supergroup          0 2017-07-30 19:52 /user/hduser/url_data_output/_SUCCESS
-rw-r--r--   1 hduser supergroup        117 2017-07-30 19:52 /user/hduser/url_data_output/part-00000
hduser@mint /usr/local/hadoop $ bin/hadoop fs -cat /user/hduser/url_data_output/part-00000
www.taobao.com  3
www.taobao.com/example.html     1
www.taobao.com/index.html       2
www.tmall.com   1
www.tmall.com/index.xml 1
```
## Stop Hadoop
```
hduser@mint /usr/local/hadoop $ sbin/stop-dfs.sh
Stopping namenodes on [localhost]
localhost: stopping namenode
localhost: stopping datanode
Stopping secondary namenodes [0.0.0.0]
0.0.0.0: stopping secondarynamenode
hduser@mint /usr/local/hadoop $ sbin/stop-yarn.sh
stopping yarn daemons
stopping resourcemanager
localhost: stopping nodemanager
```
# About the Program
The URL counter program is based on [Writing an Hadoop MapReduce Program in Python](http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/), with some modification. Besides, we add [unit test case](https://github.com/slxiao/URLCounter/blob/master/tst/run_tests.py) for the program, which helps us validate the correctness of the python scripts before running them inside hadoop. We also provide Makefile for the program, by running `make test` under the root directory, we can get the unit test results.

```
mint@mint:~/workspace/URLCount$ make test
run unit test cases of URLcount
python ./tst/run_tests.py
.
----------------------------------------------------------------------
Ran 1 test in 0.135s

OK
```
