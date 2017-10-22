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
import sys


class database_manager(object):
    def __init__(self,db_fname):

        self.conn = None
        self.cursor = None

        # Open initial connection to DB
        if db_fname:
            self.db_open(db_fname)

        # Commit and close initial connection to DB
        self.conn.commit()
        #self.cursor.close()
        #self.conn.close()


    def db_open(self, db_fname):
        # Try connecting to the DB
        try:
            self.conn = sqlite3.connect(db_fname);
            self.cursor = self.conn.cursor()

        except sqlite3.Error as e:
            print("Error connecting to {} Database".format(db_fname))


    def db_query_succ(self,table_name, column_1, value_1, column_2, value_2):
        self.cursor.execute('SELECT * FROM Raw_Data WHERE ? = ? AND NOT ? = ?', (column_1, value_1, column_2, value_2))
        query_list = self.cursor.fetchall()
        create_db_table(table_name, query_list)


    def db_query_other(self,table_name, column_name, value):
        self.cursor.execute('SELECT * FROM Raw_Data WHERE ? = ?', (column_name, value))
        query_list = self.cursor.fetchall()
        create_db_table(table_name, query_list)


    def db_create_table(self, db_table, db_columns, db_data):
        # Open connection to DB
        #self.db_open(db_fname)

        # Create table
        self.cursor.execute("""CREATE TABLE {} {}""".format(db_table,tuple(db_columns)))

        # Commit and close initial connection to DB
        self.conn.commit()
        #self.cursor.close()
        #self.conn.close()

        # Call db_insert to put data into table after creating it
        self.db_insert(db_table, db_data)

        return


    def db_insert(self, db_table, db_data):
        # Open connection to DB
        #self.db_open(db_fname)

        # Insert data into table
        self.cursor.executemany("""INSERT INTO {} {}""".format(db_table, tuple(db_data)))

        # Commit and close initial connection to DB
        self.conn.commit()
        #self.cursor.close()
        #self.conn.close()


    def __del__(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()


def csv_read(csv_fname, expected_columns):

    # Read in csv as DictReader, read in column names, read in data
    with open(csv_fname, 'r') as csv_file:

        csv_data = []

        csv_reader = csv.reader(csv_file)
        csv_columns = next(csv_reader)

        # Check column names are as expected
        if set(sorted(expected_columns)) == set(sorted(csv_columns)):
            csv_data = list(tuple(row) for row in csv_reader)
            return expected_columns, csv_data

        # Check if column names are a subset of expected
        elif set(sorted(expected_columns)) < set(sorted(csv_columns)):
            csv_data = list(tuple(row) for row in csv_reader)
            return csv_columns, csv_data

        # Throw an erros if column names are not as expected or subset of expected
        else:
            csv_data = []
            raise ValueError('CSV Data Error')
            return expected_columns, csv_data


def main():

    # Declare table column name variables
    expected_columns = ['USER_NAME','CALLING_STATION_ID','SELECTED_AZN_PROFILE']
    bypass_columns = ['USER_NAME', 'MAC_ADDRESS','MAC_OUI','MAC_VENDOR','ENDPOINTMATCHEDPROFILE','SWITCH','PORT','SWITCH_PORT','DESK_LOCATION']
    failed_columns = ['USER_NAME', 'MAC_ADDRESS','MAC_OUI','MAC_VENDOR','ENDPOINTMATCHEDPROFILE','SWITCH','PORT','SWITCH_PORT','DESK_LOCATION']
    guest_columns = ['USER_NAME', 'MAC_ADDRESS','MAC_OUI','MAC_VENDOR','ENDPOINTMATCHEDPROFILE','SWITCH','PORT','SWITCH_PORT','DESK_LOCATION']

    # Print program introduction lines
    print ('Cisco ISE Report Script\n')
    print ('This is a script designed to read in a .csv file from a Cisco ISE Report and analyse the file\n')

    # Read site code in from user input and store in variable
    site_code = input('Please enter the data site code for the report: ')

    # Read date in from user input and create database filename
    report_db_fname = input('Using the following date format \'YYYYMMDD\', please enter the report date: ') + '_' + site_code + '_ISE_Report.db'

    # While loop used to test filename is valid within the current directory
    while os.path.isfile(report_db_fname):
        print ('Database file already exists for ' + report_db_fname)
        report_db_fname = input('Please enter a new report date: ') + '_ISE_Report.db'

    # Prompt user for input CSV filename
    csv_fname = input('Please enter the input filename: ')

    # Open CSV file, read in columns, read in data
    try:
        db_columns, db_raw_data = csv_read(csv_fname,expected_columns)
    except ValueError:
        print ("CSV file is not as expected - uncrecognised column names detected. Check the file name is correct.")
        sys.exit()

    ##### CREATE TABLES #####
    # Initial connection to DB
    report_db = database_manager(report_db_fname)
    # Raw_Data tale
    report_db.db_create_table('Raw_Data', db_columns, db_raw_data)

    # Succ table


    # Bypass table

    # Failed table



    # Run queries and create new tables based on query returns
    # e.g. Query Raw_Data for all successful authentications, create succ table from query of all successful authentications
    blank = ''

    #database.query_db_table('Succ', 'SELECTED_AZN_PROFILE', 'Full_corporate_access')


    # Close connection to database
    database.__del__


if __name__ == '__main__':
    main()
