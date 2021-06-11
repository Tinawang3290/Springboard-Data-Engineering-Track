
#### 1. Is the data homogenous in each column? 

The data is not homogeneous in some columns, it contains mixed data types that need the data types to be specified. The number of the columns are NOT aligned.
```
Expected 31 fields in line 1685049, saw 33`
```

#### 2. How do you anticipate this data will be used by data analysts and scientists downstream? 

- Use pandas and numpy to organize the data for data scientists to leverage jupyter notebook for data exploration and model building 
- write into Azure mysql for data analysis.

#### 3. Does your answer to the last question give you an indication of how you can store the data for optimal querying speed and storage file compression?

Given the large size of the data, we need to scrap the data from web and send it to Azure database directly
Store the data in specified type and length.

#### 4. What cleaning steps do you need to perform to make your dataset ready for consumption? 
5. What wrangling steps do you need to perform to enrich your dataset with additional information?

- Add the header to the raw data in csv.file.
- Fill some of the missing values with 0.
- Correct the columns with the mixed data types
- Add the primary key to the origination file  

### Bugs occured during the data cleaning process
```
Error while connecting to MySQL: 1054 (42S22): Unknown column 'nan' in 'field list'
```
- solution: source_origination_data = source_origination_data.where(pd.notnull(source_origination_data), None)

```
1292 (22007): Incorrect date value: '202001' for column 'First_Payment_Date' at row 1 
```
- Solution: add string_to_date to the column, 
for i, row in source_origination_data.iterrows():
    insert_origination_data = """INSERT INTO Freddie_Mac_File.Freddie_Mac_Origination_File
        VALUES (%s, string_to_date(%s), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
```
Error while connecting to MySQL Error tokenizing data. C error: Expected 31 fields in line 24, saw 32
```
- Solution: pass ‘error_bad_lines=False’ and  ‘engine='python’’ as parameter to his function. the source_origination_data = pd.read_csv(file_path_csv[0], engine='python', header=None, error_bad_lines=False)

```
Error while connecting to MySQL: 1046 (3D000): No database selected
```
- Solution: Pending



### An Entity-Relationship diagram for your data mode

![Screen Shot 2021-06-10 at 9 26 53 PM](https://user-images.githubusercontent.com/37784402/121630820-b774e900-ca32-11eb-946e-44f30dfb55ce.png)

### A Jupyter Notebook demonstrating the steps that you performed in the exploration of the dataset
Ongoing

### A write-up of the insights from data exploration 

Ongoing

### A write-up explaining how you plan to store the data for optimal query speed and compression of storage files


