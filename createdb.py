import csv
import sqlite3

# Create or connect to the database
sqlite_conn = sqlite3.connect('MyHospital.db')
print("Database connected")

# Create a cursor object
conn = sqlite_conn.cursor()
# Print sqlite version
dbversion = conn.execute("select sqlite_version();")
print("SQLite Database Version is: ", dbversion.fetchall(), "\n")

# Ceate hospital table
conn.execute(''' CREATE TABLE IF NOT EXISTS Hospital1
            (Hospital_id INT PRIMARY KEY NOT NULL UNIQUE,
             Hospital_Name TEXT NOT NULL,
             Bed_count INT NOT NULL);''')

# Display the structure of the hospital table
ht_info = conn.execute("PRAGMA table_info('Hospital1');")
print(" \t Hospital Table Structure ")
print("__________________________________________\n")
for x in ht_info.fetchall():
    print(x)

# Read from csv file
with open('D:\hospitaldb\hospitals.csv', 'r') as hospitalrec:
    h_reader = csv.reader(hospitalrec)

    next(h_reader)  # Skip the first row

    # insert records line by line
    for rec in h_reader:
        conn.execute("INSERT OR REPLACE INTO Hospital1 VALUES (?, ?, ?);", rec)
        sqlite_conn.commit()
print("Records added")

# Create Table
conn.execute(''' CREATE TABLE IF NOT EXISTS Doctor1
            (  Doctor_id INT PRIMARY KEY NOT NULL,
              Doctor_Name TEXT NOT NULL,
              Hospital_id INT NOT NULL,
              Date_joined TEXT NOT NULL,
              Speciality TEXT NOT NULL,
              Salary INT NOT NULL,
              Experience TEXT NOT NULL,
              Email TEXT NOT NULL,
              UNIQUE(Doctor_id, Email)
              FOREIGN KEY (Hospital_id)
                REFERENCES Hospital1 (Hospital_id) );''')

# Display Table structure
dt_info = conn.execute("PRAGMA table_info('Doctor1');")
print(" \n\t Doctor Table Structure ")
print("_____________________________________\n")
for d in dt_info.fetchall():
    print(d)

# Read from csv file
with open('D:\hospitaldb\doctors.csv', 'r') as docrec:
    d_reader = csv.reader(docrec)

    next(d_reader)  # dkip first ecord
    for rec in d_reader:
        conn.execute(
            "INSERT OR REPLACE INTO Doctor1 VALUES (?, ?, ?, ?, ?, ?, ?, ?);", rec)
        sqlite_conn.commit()
print("Records added")


def my_join():
    # Query to create inner join
    hos_join = conn.execute('''SELECT * FROM Doctor1 INNER JOIN Hospital1 
                        ON Hospital1.Hospital_id = Doctor1.Hospital_id;''')
    # Display records
    print(" \n\t\t\t\t Records ")
    print("______________________________________________________________________________\n")
    for j in hos_join.fetchall():
        print(j, "\n")


# call the function
my_join()

# close cursor
conn.close()
