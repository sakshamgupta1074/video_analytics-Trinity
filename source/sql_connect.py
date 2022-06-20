#!/usr/bin/env python

__author__      = "Team Trinity"

import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Electronics',
                                         user='pynative',
                                         password='pynative@#29')

    mySql_Create_Table_Query = """CREATE TABLE SBI_CCTV_INFO (Sno int PRIMARY KEY, Count_of_people int, Hazardous_objects timestamp, Fire_Theft_incidents timestamp, Known_Miscreants varchar(100), Location Varchar(100), Time timestamp, Known_Employee_ID Varchar(100), Interruption_Detection timestamp);"""

    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("Laptop Table created successfully ")

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")