import mysql.connector
import pandas as pd


def get_db_connection() -> object:
    """
    Connect to mysql database using credentials
    :rtype: object
    """
    connection = None
    try:
        connection = mysql.connector.connect(user='your username',
                                             password='your password',
                                             host='localhost',
                                             port='3306',
                                             database='ticket_system')
    except Exception as error:
        print("Error while connecting to database for job tracker", error)
    return connection


def load_third_party(conn, file_path_csv):
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
        DROP DATABASE IF EXISTS ticket_system;
        CREATE DATABASE ticket_system;
        USE ticket_system;
        CREATE TABLE ticket_sales(
            ticket_id INT,
            trans_date DATE,
            event_id INT,
            event_name VARCHAR(50),
            event_date DATE,
            event_type VARCHAR(10),
            event_city VARCHAR(20),
            customer_id INT,
            price DECIMAL(7,2),
            num_tickets INT,
            PRIMARY KEY(ticket_id) 
            );
        """
        source_data = pd.read_csv(file_path_csv, header=None)
        # cursor.execute(sql_ddl_statement)
        # cursor.execute('SHOW DATABASES')
        print('Database and table are created.')
        for _ in cursor.execute(sql_ddl_statement, multi=True):
            pass
        for i, row in source_data.iterrows():
            insert_data = """INSERT INTO ticket_system.ticket_sales
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
            # print(row)
            cursor.execute(insert_data, tuple(row))
        conn.commit()
        cursor.close()
    except Exception as e:
        cursor.close()
        print("Error while connecting to MySQL", e)


def query_popular_tickets(conn):
    """
    - Get the most popular ticket in the past month
    :param conn:
    :return:
    """
    sql_statement = '''SELECT event_name FROM(
    SELECT event_name, total_num, DENSE_RANK() OVER (ORDER BY total_num DESC) AS rk
    FROM (SELECT event_name, SUM( num_tickets) AS total_num
    FROM ticket_system.ticket_sales
    GROUP BY event_name) a) b
    WHERE rk =1;
    '''
    cursor = conn.cursor()
    cursor.execute(sql_statement)
    records = cursor.fetchall()
    cursor.close()
    return records


if __name__ == '__main__':
    conn = get_db_connection()
    file_path_csv = '~/downloads/third_party_sales_1.csv'
    load_third_party(conn, file_path_csv)
    print(query_popular_tickets(conn))

