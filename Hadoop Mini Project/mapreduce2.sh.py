hadoop jar /usr/local/Cellar/hadoop/3.3.1/libexec/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file /Users/tinawang/PycharmProjects/pythonProject/Hadoop_Mapreduce_Mini_Project/Mapper2.py -mapper 'python3 Mapper2.py' \
-file  /Users/tinawang/PycharmProjects/pythonProject/Hadoop_Mapreduce_Mini_Project/Reducer2.py -reducer 'python3 Reducer2.py' \
-input /hadoop_project_folder/output1 -output /hadoop_project_folder/output2
