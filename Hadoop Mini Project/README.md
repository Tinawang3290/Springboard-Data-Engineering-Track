### Objectives
With this mini-project, we will utilize MapReduce jobs in Python to create a solution for a
real-life data problem. This will strengthen your mindset for leveraging a MapReduce processing
model to process large scale data, and your capability to break down a complex problem into
smaller tasks.

### Hadoop Setup In The Pseudo-distributed Mode (Mac OS)
https://towardsdatascience.com/installing-hadoop-on-a-mac-ec01c67b003c

- First, install HOMEBREW and JAVA
Please follow this instruction to use Homebrew to install JAVA/OPENJDK: https://gist.github.com/gwpantazes/50810d5635fc2e053ad117b39b597a14
After downloading JAVA, need to run `sudo ln -sfn /usr/local/opt/openjdk/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jd` command to start java.

Check below to set java home environment variable on Mac os X.
https://mkyong.com/java/how-to-set-java_home-environment-variable-on-mac-os-x/
```
(venv) (base) F0140:pythonProject tinawang$ ls -l /usr/bin/java
-rwxr-xr-x  1 root  wheel  138896 Jan  1  2020 /usr/bin/java
(venv) (base) F0140:pythonProject tinawang$ java -version
openjdk version "16.0.1" 2021-04-20
OpenJDK Runtime Environment Homebrew (build 16.0.1+0)
OpenJDK 64-Bit Server VM Homebrew (build 16.0.1+0, mixed mode, sharing)
(venv) (base) F0140:pythonProject tinawang$ ls -l /etc/alternatives/java
ls: /etc/alternatives/java: No such file or directory
(venv) (base) F0140:pythonProject tinawang$ nano ~/.zshenv
(venv) (base) F0140:pythonProject tinawang$ source ~/.zshenv
(venv) (base) F0140:pythonProject tinawang$ echo $JAVA_HOME
/usr/local/Cellar/openjdk/16.0.1/libexec/openjdk.jdk/Contents/Home
```
what is inside  `nano ~/.zshenv`:
```
export JAVA_HOME=$(/usr/libexec/java_home)
export HADOOP_VERSION=3.3.1
export HADOOP_HOME=usr/local/Cellar/hadoop/3.3.1
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export PATH=$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$PATH


```

- Once HOMEBREW and JAVA are installed, then run: `brew install hadoop` command in terminal. 

Follow this post https://stackoverflow.com/questions/51808588/run-hadoop-in-the-mac-os  
https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html

A. brew search hadoop
`==> Formulae
hadoop ✔
` 

B. Go to hadoop base directory, `usr/local/Cellar/hadoop/3.3.1/libexec/etc/hadoop` and under this folder, it requires to modify these files:  
i). `hadoop-env.sh`
Add
```
export HDFS_DATANODE_USER=root 
export HADOOP_SECURE_DN_USER=root  
export HDFS_NAMENODE_USER=root    
export HDFS_SECONDARYNAMENODE_USER=root  
export YARN_RESOURCEMANAGER_USER=root  
export YARN_NODEMANAGER_USER=root 

export HADOOP_OPTS="$HADOOP_OPTS -Djava.net.preferIPv4Stack=true -Djava.security.krb5.realm= -Djava.security.krb5.kdc="
export JAVA_HOME = /usr/local/opt/openjdk
```

(ii). core-site.xml

Then configure HDFS address and port number, open core-site.xml, input following content in configuration tag
```
<!-- Put site-specific property overrides in this file. -->
 <configuration>
    <property>
        <name>hadoop.tmp.dir</name>
        <value>/usr/local/Cellar/hadoop/hdfs/tmp</value>
        <description>A base for other temporary directories.</description>
    </property>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:8020</value>
    </property>
</configuration>
```

(iii). mapred-site.xml  

Configure MapReduce to use YARN, first copy mapred-site.xml.template to mapred-site.xml, and open mapred-site.xml, add
```
<configuration>
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
    <property>
        <name>yarn.app.mapreduce.am.env</name>
        <value>HADOOP_MAPRED_HOME=/Users/Masser/hadoop</value>
    </property>
    <property>
        <name>mapreduce.map.env</name>
        <value>HADOOP_MAPRED_HOME=/Users/Masser/hadoop</value>
    </property>
    <property>
        <name>mapreduce.reduce.env</name>
        <value>HADOOP_MAPRED_HOME=/Users/Masser/hadoop</value>
    </property>
</configuration>
```

(iv). hdfs-site.xml

Set HDFS default backup, the default value is 3, we should change to 1, open hdfs-site.xml, add
```
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
</configuration> 
```
(v). yarn-site.xml  

To walk through the org.apache.hadoop.yarn.exceptions.InvalidAuxServiceException: The auxService:mapreduce_shuffle does not exist, we need to modify the file,
```
<configuration>
    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>
    <property>
        <name>yarn.nodemanager.aux-services.mapreduce_shuffle.class</name>
        <value>org.apache.hadoop.mapred.ShuffleHandler</value>
    </property>
</configuration>
```

C. Setup a pass-phraseless SSH and Authorize the generate SSH keys:
```
$ ssh-keygen -t rsa -P ''  
$ cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
```
Finally, Enable Remote Login in (System Preference->Sharing), Just click “remote login”.

Test ssh at localhost: It should not prompt for a password

$ ```ssh localhost```

Last login: Sun Jul 11 11:54:01 2021

D. Format the distributed file system with the below command before starting the Hadoop daemons. So that we can put our data sources into the hdfs file system while performing the map-reduce job
https://www.youtube.com/watch?v=TMKRMJvsoOw 

$ ```hdfs namenode -format```
step1 : ```bin/hdfs namenode -format```
step 2: start all hadoop processes: ```sbin/start-dfs.sh```
step 3: NameNode: http://localhost:9870/
step 4: start yarn: ```sbin/start-yarn.sh``
Step 5: resourceManager: http://localhost:8088/
type in command ```jps``` to check all the Hadoop daemons like NameNode, DataNode, ResourceManager, NodeManager etc. which are running on the machine
Step 6: stop all hadoop process: sbin/stop-all.sh

#### Note: issues might come up when run ```sbin/start-dfs.sh``` command.

https://docs.cloudera.com/HDPDocuments/HDP2/HDP-2.6.4/bk_reference/content/hdfs-ports.html 





