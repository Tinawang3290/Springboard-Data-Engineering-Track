hadoop jar /usr/local/Cellar/hadoop/3.3.1/libexec/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file /Users/tinawang/PycharmProjects/pythonProject/Hadoop_Mapreduce_Mini_Project/Mapper1.py -mapper 'python3 Mapper1.py' \
-file  /Users/tinawang/PycharmProjects/pythonProject/Hadoop_Mapreduce_Mini_Project/Reducer1.py -reducer 'python3 Reducer1.py' \
-input /hadoop_project_folder/Hadoop_Mapreduce_Mini_Project/data.csv -output /hadoop_project_folder/output1
