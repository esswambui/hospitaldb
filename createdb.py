import sqlite3
import csv


sqlite_conn = sqlite3.connect('MyDatabase.db')

conn = sqlite_conn.cursor()

# Print sqlite version
dbversion = conn.execute("select sqlite_version();")
print("SQLite Database Version is: ", dbversion.fetchall(), "\n")

# Ceate hospital table
conn.execute(''' CREATE TABLE IF NOT EXISTS Hospital
            (Hospital_id INT PRIMARY KEY NOT NULL,
             Hospital_Name TEXT NOT NULL,
             Bed_count INT NOT NULL);''')

# Table structure
ht_info = conn.execute("PRAGMA table_info('Hospital');")
print(" \t Hospital Table Structure ")
print("_____________________________________\n")
for x in ht_info.fetchall():
    print(x, "\n")

# Read from csv file
with open('D:\hospitaldb\hospitals.csv', 'r') as hospitalrec:
    h_reader = csv.reader(hospitalrec)
    next(h_reader)
    for rec in h_reader:
        conn.execute("INSERT INTO Hospital VALUES (?, ?, ?);", rec)
        sqlite_conn.commit()
print("Records added")

# Create Table
conn.execute(''' CREATE TABLE IF NOT EXISTS Doctor
            (  Doctor_id INT PRIMARY KEY NOT NULL,
              Doctor_Name TEXT NOT NULL,
              Hospital_id INT NOT NULL,
              Date_joined TEXT NOT NULL,
              Speciality TEXT NOT NULL,
              Salary INT NOT NULL,
              Experience TEXT NOT NULL,
              FOREIGN KEY (Hospital_id)
                REFERENCES Hospital (Hospital_id) );''')

# Table structure
dt_info = conn.execute("PRAGMA table_info('Doctor');")
print(" \n\t Doctor Table Structure ")
print("_____________________________________\n")
for d in dt_info.fetchall():
    print(d, "\n")

# Read from csv file
with open('D:\hospitaldb\doctors.csv', 'r') as docrec:
    d_reader = csv.reader(docrec)
    next(d_reader)
    for rec in d_reader:
        conn.execute(
            "INSERT INTO Doctor VALUES (?, ?, ?, ?, ?, ?, ?);", rec)
        sqlite_conn.commit()
print("Records added")

conn.close()
