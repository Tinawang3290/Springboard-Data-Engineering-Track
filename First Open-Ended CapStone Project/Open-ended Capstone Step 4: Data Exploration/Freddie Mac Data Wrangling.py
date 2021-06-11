#  pycron, time
import os
import urllib.request
import zipfile
import requests
import mysql.connector
import pandas as pd
# from bs4 import BeautifulSoup
import csv


def login_website(user_name, password, login_url, download_url):
    '''
    Credentials and agreements need to be input/reached to log into the Freddie Mac web.
    '''
    with requests.Session() as s:
        s.get(login_url)
        php_session_cookie = s.cookies['PHPSESSID']
        login_payload = {'username': user_name, 'password': password, 'cookie': php_session_cookie}
        response_login = s.post(login_url, login_payload)
        download_payload = {'accept': 'Yes', 'action': 'acceptTandC', 'acceptSubmit': 'Continue',
                            'cookie': php_session_cookie}
        download_login = s.post(download_url, download_payload)
    print(" SUCCESS   : Login into FreddieMac.com successfully! ")


def create_directory(dir_name):
    '''
    1. Create a local dictionary if not exist to store downloaded files.
    2. Raise error if any without stopping the code execution
    '''
    current_directory = os.getcwd()
    if not os.path.exists(dir_name):
        try:
            os.makedirs(dir_name)
        except os.errno != errno.EEXIST:  # if the error is not the file exists code, then flag it.
            raise
    print(" SUCCESS   : {} directory creation successfully!".format(dir_name))


def get_data_from_url(dir_name, unzipped_dir_name, start_year, end_year):
    '''
    1. Identify all the available data in years on the web to ensure that the data can be download based on any requested date range
    2. Download the zipped files to the designated directory from the web once logged in with requested date range
    3. Unzip the zipped files to its readable format
    4. Save the unzipped files to the designated directory that created
    5. Close and remove the zipped files from the same directory
    '''
    for year in range(start_year, end_year + 1):
        download = urllib.request.urlretrieve(
            'https://freddiemac.embs.com/FLoan/Data/historical_data_{}.zip'.format(year),
            os.path.join(dir_name, 'historical_data_{}.zip'.format(year)))
        unzip_file = zipfile.ZipFile(os.path.join(dir_name, 'historical_data_{}.zip'.format(year)), 'r')  # unzip file
        unzip_file.extractall(unzipped_dir_name)  # write unzipped file into the designated directory
        for item in os.listdir(unzipped_dir_name):  # loop through all the items in the directory
            if item.endswith('.zip'):  # check for '.z' extension
                file_name = unzipped_dir_name + '/' + item
                zip_ref = zipfile.ZipFile(file_name)  # create zip file object
                zip_ref.extractall(unzipped_dir_name)  # extract unzipped file into the designated directory
                zip_ref.close()  # close file
                os.remove(file_name)  # delete zipped filed
        os.remove(os.path.join(dir_name, 'historical_data_{}.zip'.format(year)))
    print(" SUCCESS   : {} historical data files have been downloaded and unzipped successfully!".format(year))


def write_into_consolidated_file(dir_name, unzipped_dir_name, start_year, end_year):
    '''
    1. Navigate to the source files and then read the data from the files
    2. Create the consolidated files, then write the data from the source files to the designated destination files.
    3. Remove source files ensure the files won't be incremented with the same files for each run
    '''
    for year in range(start_year, end_year + 1):
        for item in os.listdir(unzipped_dir_name):  # loop through all the items in the directory
            if item.startswith('historical_data_' + str(year)) and item.endswith('.txt'):
                source_file_name = unzipped_dir_name + '/' + item
                target_file_name = dir_name + '/unprocessed_consolidated_historical_data_orig_file.csv'  # create origination file directory to store the consolidated data
                with open(source_file_name, 'r') as sourceFile:  # open source file
                    content = sourceFile.read()  # read the source file
                    content = content.replace('|', ',')
                with open(target_file_name,
                          'a') as destinationCsvFile:  # consolidate all the files and write into the target file
                    destinationCsvFile.write(content)
            else:
                source_file_name = unzipped_dir_name + '/' + item
                target_file_name = dir_name + '/unprocessed_consolidated_historical_data_svcg_file.csv'  # create servicing file directory to store the consolidated data
                with open(source_file_name, 'r') as sourceFile:  # open source file
                    content = sourceFile.read()  # read the source file
                    content = content.replace('|', ',')
                with open(target_file_name,
                          'a') as destinationCsvFile:  # consolidate all the files and write into the target file
                    destinationCsvFile.write(content)
            # os.remove(source_file_name)
    print(" SUCCESS   : consolidated files have been created successfully!")


def scheduler():
    '''
    use cron scheduler to schedule the script for downloads to run automatically.
    '''
    while True:
        if pycron.is_now('0 4 * * *'):  # True Every Sunday at 04:00
            print('running backup')
            time.sleep(3600)  # The process should take at least 1 hour to avoid running twice given large amount of data
        else:
            time.sleep(1800)  # Check again in 30 mins

#  To save data to the database
def get_db_connection() -> object:
    """
    Connect to mysql database using credentials
    :rtype: object
    """
    connection = None
    try:
        connection = mysql.connector.connect(user='root',
                                             password='Kyleling1220@',
                                             host='localhost',
                                             port='3306')

    except Exception as error:
        print("Error while connecting to database for job tracker", error)
    return connection


def load_to_database(conn, file_path_csv):
    """
    - Create the database and table
    - Use DataFrame to read CSV source file and insert rows into created table
    :param conn:
    :param file_path_csv:
    :return:
    """

    try:
        cursor = conn.cursor()
    # [Iterate through the CSV file and execute insert statement]
        sql_ddl_statement = """
        DROP DATABASE IF EXISTS Freddie_Mac_File;
        CREATE DATABASE Freddie_Mac_File;
        USE Freddie_Mac_File;
        DROP TABLE IF EXISTS Freddie_Mac_Origination_File; 
        CREATE TABLE IF NOT EXISTS Freddie_Mac_Origination_File(
            Credit_Score INT(4),
            First_Payment_Date DATE(6),
            First_Time_Homebuyer_Flag VARCHAR(10),
            Maturity_Date DATE,
            MSA INT,
            Mortgage_Insurance_Percentage DECIMAL(7,2),
            Number_Of_Units INT, 
            Occupancy_Status VARCHAR(10),
            Original_CLTV DECIMAL(7,2), 
            Original_DTI_Ratio DECIMAL(7,2),
            Original_UPB DECIMAL(10,2), 
            Original_LTV DECIMAL(7,2),
            Original_Interest_Rate DECIMAL(7,2), 
            Channel VARCHAR(10), 
            PPM_Flag VARCHAR(10), 
            Product_Type VARCHAR(10),
            Property_State VARCHAR(10), 
            Property_Type VARCHAR(10),
            Postal_Code INT, 
            Loan_Sequence_Number VARCHAR(12) ,
            Loan_Purpose VARCHAR(25), 
            Original_Loan_Term DECIMAL(7,2),
            Number_Of_Borrowers INT(1), 
            Seller_Name VARCHAR(60),
            Servicer_Name VARCHAR(60), 
            Super_Conforming_Flag VARCHAR(25),
            Pre_HARP_Loan_Sequence_Number VARCHAR(25),
            Program_indicator VARCHAR(10), 
            HARP_Indicator VARCHAR(2),
            Property_Valuation_Method INT(1), 
            Interest_Only_Indicator VARCHAR(2),
            PRIMARY KEY(Loan_Sequence_Number) 
            );
        DROP TABLE IF EXISTS Freddie_Mac_Servicing_File;
        CREATE TABLE IF NOT EXISTS Freddie_Mac_Servicing_File(
            Loan_Sequence_Number VARCHAR(12), 
            Monthly_Reporting_Period DATE,
            Current_Actual_UPB DECIMAL(12,2), 
            Current_Loan_Delinquency_Status VARCHAR(3),
            Loan_Age INT(3), 
            Remaining_Months_For_Legal_Maturity INT(3),
            Repurchase_Flag VARCHAR(1), 
            Modification_Flag VARCHAR(1),
            Zero_Balance_Code INT(2), 
            Zero_Balance_Effective_Date DATE,
            Current_Interest_Rate DECIMAL(8,3), 
            Current_Deferred_UPB DECIMAL(12),
            Due_Date_of_Last_Paid_Installment DATE, 
            MI_Recoveries DECIMAL(12,2),
            Net_Sales_Proceeds VARCHAR(14), 
            Non_MI_Recoveries DECIMAL(12,2),
            Expenses DECIMAL(12,2), 
            Legal_Costs DECIMAL(12,2),
            Maintenance_And_Preservation_Costs DECIMAL(12,2), 
            Taxes_And_Insurance DECIMAL(12,2),
            Miscellaneous_Expenses DECIMAL(12,2), 
            Actual_Loss_Calculation DECIMAL(12,2),
            Modification_Cost DECIMAL(12,2), 
            Step_Modification_Flag VARCHAR(1),
            Deferred_Payment_Plan VARCHAR(1), 
            Estimated_Loan_to_Value INT(4),
            Zero_Balance_Removal_UPB DECIMAL(12,2), 
            Delinquent_Accrued_Interest DECIMAL(12,2),
            Delinquency_Due_to_Disaster VARCHAR(1), 
            Borrower_Assistance_Status_Code VARCHAR(1),
            FOREIGN KEY (Loan_Sequence_Number) REFERENCES Freddie_Mac_Origination_File(Loan_Sequence_Number) ON DELETE CASCADE
            );
        """
        # cursor.execute(sql_ddl_statement)
        print(cursor.execute('SHOW DATABASES'))
        print("SUCCESS   : Database and table have been created successfully.")
        # for _ in cursor.execute(sql_ddl_statement, multi=True):
        #     pass
        source_origination_data = pd.read_csv(file_path_csv[0], engine='python', header=None, error_bad_lines=False)
        source_origination_data = source_origination_data.where(pd.notnull(source_origination_data), None)
        print(source_origination_data.shape)
        for i, row in source_origination_data.iterrows():
            insert_origination_data = """INSERT INTO Freddie_Mac_File.Freddie_Mac_Origination_File
                VALUES (%s, string_to_date(%s), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
            cursor.execute(insert_origination_data, tuple(row))

            # print(row)
        # for j in range(len(file_path_csv)):
        #     if "origination" in file_path_csv[j]:
        #         print('true')
        #         source_origination_data = pd.read_csv(file_path_csv[j], header=None)
        #         for _ in cursor.execute(sql_ddl_statement, multi=True):
        #             pass
        #         for i, row in source_origination_data.iterrows():
        #             insert_origination_data = """INSERT INTO Freddie_Mac_File.Freddie_Mac_Origination_File
        #                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
        #                 %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
        #             # print(row)
        #             cursor.execute(insert_origination_data, tuple(row))
        #     elif "servicing" in file_path_csv[j]:
        #         source_servicing_data = pd.read_csv(file_path_csv[j], header=None)
        #         for _ in cursor.execute(sql_ddl_statement, multi=True):
        #             pass
        #         for i, row in source_servicing_data.iterrows():
        #             insert_servicing_data = """INSERT INTO Freddie_Mac_File.Freddie_Mac_Servicing_File
        #                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
        #                 %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
        #             # print(row)
        #             cursor.execute(insert_servicing_data, tuple(row))
        conn.commit()
        cursor.close()
        print("SUCCESS   : Data has been inserted successfully!")
    except Exception as e:
        cursor.close()
        print("Error while connecting to MySQL:", e)


def start_execution():
    # login_url = 'https://freddiemac.embs.com/FLoan/secure/login.php'
    # download_url = 'https://freddiemac.embs.com/FLoan/Data/download.php'
    # base_url = 'https://freddiemac.embs.com/FLoan/Data/'
    # user_name = 'tinawang3290@gmail.com'
    # password = '@s=`Hs5J'
    # dir_name = "Freddie_Mac_downloaded_historical_data"
    # unzipped_dir_name = "Freddie_Mac_unzipped_content"
    # start_year = 2019
    # end_year = 2019
    origination_file_path_csv = '/Users/tinawang/PycharmProjects/pythonProject/Freddie_Mac_downloaded_historical_data/unprocessed_consolidated_historical_data_orig_file.csv'
    servicing_file_path_csv = '/Users/tinawang/PycharmProjects/pythonProject/Freddie_Mac_downloaded_historical_data/unprocessed_consolidated_historical_data_svcg_file.csv'
    file_path_csv = [origination_file_path_csv, servicing_file_path_csv]
    # login_website(user_name, password, login_url, download_url)
    # create_directory(dir_name)
    # create_directory(unzipped_dir_name)
    # get_data_from_url(dir_name, unzipped_dir_name, start_year, end_year)
    # write_into_consolidated_file(dir_name, unzipped_dir_name, start_year, end_year)
    conn = get_db_connection()
    load_to_database(conn, file_path_csv)


if __name__ == '__main__':
    start_execution()

    #  pycron/airflow: scheduler, linux cronjobs scheduler is much easier.
    #  consolidate into csv. file in years.
    #  add the header to csv, cloud DB.
    # Suggestions:
    # Kafka stream --> Microsoft Azure DB/
    # check on how optimize the speed
    # 50% - 60% by 6/30 --> extension

    # Note
#     Microsoft Azure noSQL (blobs), specify the cloud path ,
#     from DE perspective, take the mean of the numeric type to fill the missing data.
#     add the global identifier(timestamp, app_uuid), incremental id is ok too

