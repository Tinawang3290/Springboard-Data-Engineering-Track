### Objectives
With this mini-project, we will utilize MapReduce jobs in Python to create a solution for a
real-life data problem. This will strengthen your mindset for leveraging a MapReduce processing
model to process large scale data, and your capability to break down a complex problem into
smaller tasks.

### 1. Hadoop Setup In The Pseudo-distributed Mode (Mac OS)
Followed the below post to download and configure java, hadoop in terminal by using homebrew.
https://towardsdatascience.com/installing-hadoop-on-a-mac-ec01c67b003c 

### 2. Create Mapper and Reducer
Once the data.csv file is downloaded, move it to the disired directory:

``` 
mv ~/downloads/*.csv /Users/tinawang/PycharmProjects/pythonProject/Hadoop_Mapreduce_Mini_Project
```

- Filter out accidents with make and year.
Please refer to `Mapper1.py, Reducer1.py`

- Count number of accident occurrences for the vehicle make and year.
Please refer to `Mapper2.py, Reducer2.py`

### 3. Test the MapReduce jobs using bash pipeline
- Input below to test Mapper1.py is working. 
```
cat data.csv | python3 Mapper1.py | sort
```
<img width="542" alt="Screen Shot 2021-08-14 at 7 50 09 PM" src="https://user-images.githubusercontent.com/37784402/129465388-8910b322-ae45-42d3-b082-874db406f496.png">

- Input below to test Reducer1.py is working.
```
 cat data.csv | python3 Mapper1.py | sort | python3 Reducer1.py
```
<img width="446" alt="Screen Shot 2021-08-14 at 8 02 28 PM" src="https://user-images.githubusercontent.com/37784402/129465589-5abaf3d7-ac69-4f66-8ea2-0c1d82bf1f7e.png">

- input below to test Mapper2.py is working.
```
cat data.csv | python3 Mapper1.py | sort | python3 Reducer1.py | python3 Mapper2.py | sort
```
<img width="280" alt="Screen Shot 2021-08-14 at 8 05 25 PM" src="https://user-images.githubusercontent.com/37784402/129465679-7c28cdd4-1e49-42cc-aa68-ec0365ff3bc6.png">

- input below to test Reducer2.py is working.
```
cat data.csv | python3 Mapper1.py | sort | python3 Reducer1.py | python3 Mapper2.py | sort | python3 Reducer2.py
```
<img width="247" alt="Screen Shot 2021-08-14 at 8 05 57 PM" src="https://user-images.githubusercontent.com/37784402/129465685-c3189f87-e980-4507-9ffe-4a8f6c6b9ed2.png">

### 4. Write a shell script to run the two MapReduce jobs
Please refer to `bash_script.sh`
