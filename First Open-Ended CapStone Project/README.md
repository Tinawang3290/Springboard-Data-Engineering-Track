
In this project, we are intended to build an end to end pipeline for Collecting, Pre-Processing both Static and Streaming data, 
Build, Deploy, Monitor and Infer Real Time Machine Learning Model. Here three independent cases are used for depicting the pipeline, 
but similar steps can be used for a single use case to built an end to end Big Data and Machine Learning Pipeline.

![image](https://user-images.githubusercontent.com/37784402/117561549-9fcdcd80-b04c-11eb-93d3-5e92db6606eb.png)

Build an Big Data Pipeline for both Static and Streaming Data -> Process Data in Apache Hadoop using Hive -> Load processed data to Data Warehouse solution like Redshift and RDS like MySQL -> Collect Streaming Data using AWS Service like Kinesis Streaming and Kinesis Firehose -> Run Real Time Analysis on Live Streaming Data using Kinesis Analytics -> Build and Deploy an Image Classifier ML Model with SageMaker and API ->  Build and Deploy an Real Time Web App using Flask to infer Image Classifier.

### One: Static data
***Static data*** collected from Freddie Mac Single Family Loan Level dataset having more than one billion records of size greater than 80 GB. Date ranges from 1999 to 2020 and data are updated on a quarterly basis. Once data is uploaded and consolidated into unprocessed CSV files. EMR and Hive is used to collect and pre-process data. Processed data is then loaded to S3 for Machine Learning. Along with S3, Processed data is also loaded to SQL and Redshift from where it can be used to build Reports and Dashboards. 

![image](https://user-images.githubusercontent.com/37784402/117561089-8165d300-b048-11eb-8165-0c4fd629bdfe.png)

#### Step 1: 
sign up on Freddie Mac web and then use credentials to login https://freddiemac.embs.com/FLoan/secure/login.php, once logged in, use python script to scrap Freddie Mac Single Family Origination and Serivicing data ranging from 1999 to 2020. Given the large size of the data, we will download and extract the data from a small date range(2019-2020) to my local PC. We will need to unzip the file to its base format(.txt) and then consolidate the .txt files into Origination and Servicing csv files respectively for the next steps.
Note: we will use pycron to make a scheduler to automatically detect data updates and download the new feeds.

#### Step 2: 
The consolidated .csv files are then loaded to S3 using AWS CLI commands from the local PC. 

#### Step 3:  
Create external tables for both Raw and Processed files in Hive using S3 as file location. This is used for machine learning.

#### Step 4:  
On acquisition data, pre-processing like Date conversion is performed. It took around 140 seconds for loading 25 million records to the processed acquisition table with S3 as data location. Size of raw and processed acquisition files is 3.7 and 3.8 GB respectively.
Acquisition data is also loaded into a partitioned table on yearly basis as an optimization technique for quick Hive queries.

#### Step 5: 
Create MySQL table in AWS RDS and load the data from S3 using Sqoop in EMR Linux. 

#### Step 6: 
Create Redshift Table and pull processed data into Redshift from S3 using Copy command.

### Two: Streaming Data

Streaming data is collected from a live data generator. Live data is consumed using Kinesis Data Stream. Kinesis Data Analytics is used for Real Time data analysis and Transformation using SQL. Lambda is used in next step for data transformation and FireHose to write final data to S3. Similar pipeline can be used for Server Log analysis or Twitter analysis.

![image](https://user-images.githubusercontent.com/37784402/117562156-a90d6900-b051-11eb-9119-40a058412d3e.png)

Dummy Data is collected from random user stream URL. AWS Kinesis Family is used to collect and pre-process stream data. Similar pipeline can be used to consume large amount of live data for any specific use case. Here data is stored to S3 for further ML process, but can also route processed data to RDS, Redshift, DynamoDB & EMR from Firehose. Firehose can also directly consume stream data to avoid any latency caused by Data Stream and Analytics with the cost of not storing stream data into disk.

#### Step 1:
A Data-Stream is created using AWS Kinesis Console.

#### Step 2:
Create and execute a python script in local PC with AWS credentials to read data from Live Stream and writes to Data-Stream. Once the script is triggered successfully, Kinesis Data-Stream will be receiving records which is validated from Data-Stream Monitoring Console. Put_Record is used along with data Records and Partition Key to load data into Data-Stream in the python script.

#### Step 3:
Kinesis Analytics is used to pull Data from Kinesis Data-Stream, Execute real time Queries using SQL and Transform data as required. Analytics is able to determine the schema of input records automatically. If not, own schema can also be defined.


Post transformation, Kinesis Analytics is used to creates two different streams of data. One for SQL query Transformed data and one for Errors. These two different streams are delivered to different Firehose Delivery-Streams respectively for further route.

#### Step 4:
Once data is pushed to Firehose Delivery-Stream, a Lambda function(Python Script) is invoked to perform further data transformation on successful data from SQL transformation. In this case, a new line character is added after each record. Post transformation, Lambda function gives back transformed records to Firehose for further transfer. Failure records from previous step are directly written to S3 for later processing.

Once certain buffer size is reached that is defined during Delivery Stream setup, Delivery-Stream loads processed data to S3. Any transformation failure records by Lambda function is also written to S3 by Delivery Stream.

-- To be Continued.


