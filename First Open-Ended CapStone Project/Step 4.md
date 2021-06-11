
Error that 
Error while connecting to MySQL: 1054 (42S22): Unknown column 'nan' in 'field list'
solution: source_origination_data = source_origination_data.where(pd.notnull(source_origination_data), None)

1292 (22007): Incorrect date value: '202001' for column 'First_Payment_Date' at row 1 
Solution: add string_to_date to the column, 
for i, row in source_origination_data.iterrows():
    insert_origination_data = """INSERT INTO Freddie_Mac_File.Freddie_Mac_Origination_File
        VALUES (%s, string_to_date(%s), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);

Error while connecting to MySQL Error tokenizing data. C error: Expected 31 fields in line 24, saw 32
Solution: pass ‘error_bad_lines=False’ and  ‘engine='python’’ as parameter to his function. the source_origination_data = pd.read_csv(file_path_csv[0], engine='python', header=None, error_bad_lines=False)

Error while connecting to MySQL: 1046 (3D000): No database selected


### An Entity-Relationship diagram for your data mode

