#!/usr/bin/env python
#
# Author: Bradley Hunt
#
# This is a script designed to read in a .csv file from a Cisco ISE Report and analyse the file


### Notes: Problems to Solve
### - Assign table headers to variable to pass into table creation function
### - Assign column names to variable to pass into SELECT WHERE statements wher column name is return value
###     * Solution - Assign values to variables which will be passed into the function when it is called. Investiagte * being used
### - Provide the ability to use a signle or multiple SELECT WHERE options in a class function
### - Create another table from the output of a table query


import csv
import sqlite3
import os.path

class database_manager(object):
    def __init__(self,db_filename,csv_filename):
        self.conn = sqlite3.connect(db_filename)
        self.conn.commit()
        self.cursor = self.conn.cursor()

        self.cursor.execute("""CREATE TABLE Raw_Data (
                                DATE_TIME,
                                CALLING_STATION_ID,
                                USER_NAME,
                                SELECTED_AZN_PROFILE,
                                AUTH_PROTOCOL);
                            """)
        self.conn.commit()

        with open(csv_filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            write_db = [(i['DATE_TIME'], i['CALLING_STATION_ID'], i['USER_NAME'], i['SELECTED_AZN_PROFILE'], i['AUTH_PROTOCOL']) for i in csv_reader]

            self.cursor.executemany("""INSERT INTO Raw_Data (
                                DATE_TIME,
                                CALLING_STATION_ID,
                                USER_NAME,
                                SELECTED_AZN_PROFILE,
                                AUTH_PROTOCOL) VALUES (?,?,?,?,?);
                            """, write_db)
            self.conn.commit()

    def succ_query_db_table(self,table_name, column_1, value_1, column_2, value_2):
        self.cursor.execute('SELECT * FROM Raw_Data WHERE ? = ? AND NOT ? = ?', (column_1, value_1, column_2, value_2))
        query_list = self.cursor.fetchall()
        create_db_table(table_name, query_list)

    def other_query_db_table(self,table_name, column_name, value):
        self.cursor.execute('SELECT * FROM Raw_Data WHERE ? = ?', (column_name, value))
        query_list = self.cursor.fetchall()
        create_db_table(table_name, query_list)

    def create_db_table(self, table_name, query_list):
        self.cursor.execute("""CREATE TABLE ? (
                                DATE_TIME,
                                CALLING_STATION_ID,
                                USER_NAME,
                                SELECTED_AZN_PROFILE,
                                AUTH_PROTOCOL);
                            """)

        self.cursor.executemany("""INSERT INTO Raw_Data (
                                    DATE_TIME,
                                    CALLING_STATION_ID,
                                    USER_NAME,
                                    SELECTED_AZN_PROFILE,
                                    AUTH_PROTOCOL) VALUES (?,?,?,?,?);
                                """, query_list)

        pass

    def __del__(self):
        self.conn.close()


def main():
    # Print program introduction lines
    print ('Cisco ISE Report Script\n')
    print ('This is a script designed to read in a .csv file from a Cisco ISE Report and analyse the file\n')

    # Read date in from user input and create database filename
    db_filename = input('Using the following date format \'YYYYMMDD\', please enter the report date: ') + '_ISE_Report.db'

    # While loop used to test filename is valid within the current directory
    while os.path.isfile(db_filename):
        print ('Database file already exists for ' + db_filename)
        db_filename = input('Please enter a new report date: ') + '_ISE_Report.db'

    # Prompt user for input CSV filename
    csv_filename = input('Please enter the input filename: ')

    # Call database_manager class passing in the db_filename
    database = database_manager(db_filename,csv_filename)

    # Run queries and create new tables based on query returns
    # e.g. Query Raw_Data for all successful authentications, create succ table from query of all successful authentications
    blank = ''

    #database.query_db_table('Succ', 'SELECTED_AZN_PROFILE', 'Full_corporate_access')


    # Close connection to database
    database.__del__


if __name__ == '__main__':
    main()
