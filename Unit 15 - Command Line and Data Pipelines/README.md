### Learning Objectives:
With this-mini project, we’ll practice Python and SQL skills by creating a basic data pipelinea and learn how to use the Python database connector to perform data loading and query
databases programmatically.

#### Step 1. Install MySQL Python connector

mysql-connector-python is a MySQL database adapter in Python. It provides convenient APIs to
load and query the tables. It also has a nice tool to load CSV files into the tables. In this step,
we will need to install this Python module.

`pip3 install mysql-connector-python`

#### Step 2. Load third-party ticket sales data into MySQL database

##### 2.1 Setup database connection
In order to make a query against the database table, we need to first connect to it. A connection
can be established only when the user provides the proper target host, port, and user
credentials.

##### 2.2 Load CSV to table
You’ll find the third party vendor data in the CSV file provided to you. The CSV follows the
schema of the table. You will need to use the Python connector to insert each record of the CSV
file into the “sales” table.
![image](https://user-images.githubusercontent.com/37784402/118389392-a2956900-b5de-11eb-9e10-3910270bae1b.png)


#### Step 3. Display statistical information
After the data is loaded into the table, you can use this data to provide recommendations to the
user. For instance, recommending popular events by finding the most top-selling tickets for the
past month.

##### 3.1 Query the table and get the selected records

##### 3.2 Display the result
The records you just retrieved are formatted as a list of tuples. You need to convert the format to
display the on-screen results in a more user-friendly format.

Errors:

`Error while connecting to MySQL 2014 (HY000): Commands out of sync; you can't run this command now`
