
In this project, we are intended to build an end to end pipeline for Collecting, Pre-Processing both Static/Streaming data, 
Build, Deploy, Monitor and Infer Real Time Machine Learning Model. Here three independent cases are used for depicting the pipeline, 
but similar steps can be used for a single use case to built an end to end Big Data and Machine Learning Pipeline.

Static data is collected from Freddie Mac Single Family Loan Level dataset having more than one billion records of size greater than 80 GB. EMR and Hive is used to collect and pre-process data. Processed data is then loaded to S3 for Machine Learning. 
Along with S3, Processed data is also loaded to SQL and Redshift from where it can be used to build Reports and Dashboards. 
