import requests
import os
import urllib
import zipfile
import threading
# from bs4 import BeautifulSoup
import csv
import pycron

def login_website(user_name, password, login_url, download_url):
    '''
    Credentials and agreements need to be intput/reached to log into the Freddie Mac web.
    '''
    with requests.Session() as s:
        s.get(login_url)
        php_session_cookie = s.cookies['PHPSESSID']
        login_payload = {'username':user_name, 'password': password, 'cookie': php_session_cookie}
        response_login = s.post(login_url, login_payload)
        download_payload = {'accept': 'Yes', 'action': 'acceptTandC', 'acceptSubmit': 'Continue', 'cookie': php_session_cookie}
        download_login = s.post(download_url, download_payload)
print( " SUCCESS   : Login into FreddieMac.embs.com succesfully! ")

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
    print(" SUCCESS   : {} directory creation succesfully!".format(dir_name))

def get_data_from_url(dir_name, unzipped_dir_name, start_year, end_year): 
    '''
    1. Identify all the available data in years on the web to ensure that the data can be download based on any requested date range 
    2. Download the zipped files to the designated directory from the web once logged in with requested date range
    3. Unzip the zipped files to its readable format
    4. Save the unzipped files to the designated directory that created
    5. Close and remove the zipped files from the same directory
    '''
    for year in range(start_year, end_year+1):
        download = urllib.urlretrieve('https://freddiemac.embs.com/FLoan/Data/historical_data_{}.zip'.format(year),
                                    os.path.join(dir_name,'historical_data_{}.zip'.format(year)))
        unzip_file = zipfile.ZipFile(os.path.join(dir_name,'historical_data_{}.zip'.format(year)), 'r') # unzip file
        unzip_file.extractall(unzipped_dir_name) # write unzipped file into the designated directory
        for item in os.listdir(unzipped_dir_name): # loop through all the items in the directory
            if item.endswith('.zip'): # check for '.z' extension
                file_name = unzipped_dir_name + '/' + item
                zip_ref = zipfile.ZipFile(file_name) # create zip file object
                zip_ref.extractall(unzipped_dir_name) #extract unzipped file into the designated directory
                zip_ref.close() # close file
                os.remove(file_name)  #delete zipped filed
        os.remove(os.path.join(dir_name, 'historical_data_{}.zip'.format(year)))
    print(" SUCCESS   : {} historical data files have been downloaded and unzipped succesfully!".format(year))

def write_into_consolidated_file(dir_name, unzipped_dir_name, start_year, end_year):
    '''
    1. Navigate to the source files and then read the data from the files
    2. Create the consolidated files, then write the data from the source files to the designated destination files.
    3. Remove source files ensure the files won't be incremented with the same files for each run
    '''
    for year in range(start_year, end_year+1):
        for item in os.listdir(unzipped_dir_name): # loop through all the items in the directory
            if item.startswith('historical_data_' + str(year)) and item.endswith('.txt'):
                source_file_name = unzipped_dir_name + '/' + item 
                target_file_name = dir_name + '/unprocessed_consolidated_historical_data_orig_file.csv'  #create origination file directory to store the consolidated data
                with open(source_file_name, 'r') as sourceFile: # open source file
                    content = sourceFile.read() # read the source file
                    content =  content.replace('|', ',')
                with open(target_file_name, 'a') as destinationCsvFile: # consolidate all the files and write into the target file
                    destinationCsvFile.write(content)     
            else:
                source_file_name = unzipped_dir_name + '/' + item 
                target_file_name = dir_name + '/unprocessed_consolidated_historical_data_svcg_file.csv'  #create servicing file directory to store the consolidated data
                with open(source_file_name, 'r') as sourceFile: # open source file
                    content = sourceFile.read() # read the source file
                    content =  content.replace('|', ',')
                with open(target_file_name, 'a') as destinationCsvFile: # consolidate all the files and write into the target file
                    destinationCsvFile.write(content)
            # os.remove(source_file_name)    
    print(" SUCCESS   : consolidated files have been created succesfully!")

def scheduler():
    '''
    use cron scheduler to schedule for downloads
    '''
    while True:
        if pycron.is_now('0 2 * * 0'):   # True Every Sunday at 02:00
            print('running backup')
            time.sleep(3600)               # The process should take at least 1 hour to avoid running twice given large amount of data
        else:
            time.sleep(1800)               # Check again in 30 mins

def start_execution():
    login_url='https://freddiemac.embs.com/FLoan/secure/login.php'
    download_url='https://freddiemac.embs.com/FLoan/Data/download.php'
    base_url =  'https://freddiemac.embs.com/FLoan/Data/'
    user_name = 'tinawang3290@gmail.com'
    password = '@s=`Hs5J'
    dir_name = "Freddie_Mac_downloaded_historical_data"
    unzipped_dir_name = "Freddie_Mac_unzipped_content"
    start_year = 2019
    end_year = 2020
    login_website(user_name, password, login_url, download_url)
    create_directory(dir_name)
    create_directory(unzipped_dir_name)
    get_data_from_url(dir_name, unzipped_dir_name, start_year, end_year)
    write_into_consolidated_file(dir_name, unzipped_dir_name, start_year, end_year)

if __name__ == '__main__':
    start_execution()

    










