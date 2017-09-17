#!/usr/bin/env python
#
# Author: Bradley Hunt
#
# This is a script designed to read in a .csv file from a Cisco ISE Report and analyse the file

import csv
import sqlite3
import os.path

def create_db():
    db_filename = input('Please enter the report date: ') + '_ISE_Report.db'

    while os.path.isfile(db_filename):
        print ('Database file already exists for ' + db_filename)
        db_filename = input('Please enter a new report date: ') + '_ISE_Report.db'

    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE Location (
                        DATE_TIME,
                        CALLING_STATION_ID,
                        USER_NAME,
                        SELECTED_AZN_PROFILE,
                        AUTH_PROTOCOL);
                    """)
    conn.commit()
    conn.close()

    return db_filename


def read_csv_into_db(db_filename):
    filename = input('Please enter the input filename: ')

    with open(filename, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        write_db = [(i['DATE_TIME'], i['CALLING_STATION_ID'], i['USER_NAME'], i['SELECTED_AZN_PROFILE'], i['AUTH_PROTOCOL']) for i in csv_reader]

        conn = sqlite3.connect(db_filename)
        cursor = conn.cursor()
        cursor.executemany("""INSERT INTO Location (
                            DATE_TIME,
                            CALLING_STATION_ID,
                            USER_NAME,
                            SELECTED_AZN_PROFILE,
                            AUTH_PROTOCOL) VALUES (?,?,?,?,?);
                        """, write_db)
        conn.commit()
        conn.close()

def main():
    print ('Cisco ISE Report Script\n\n')
    print ('This is a script designed to read in a .csv file from a Cisco ISE Report and analyse the file')

    db_filename = create_db()
    read_csv_into_db(db_filename)


if __name__ == '__main__':
    main()
