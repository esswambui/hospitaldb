import sqlite3

conn = sqlite3.connect(':memory:')

conn.execute(''' CREATE TABLE IF NOT EXISTS Students
            (ID INT PRIMARY KEY NOT NULL,
             NAME TEXT  NOT NULL,
             AGE INT    NOT NULL,
             ADDRESS    CHAR(100),
             SALARY     REAL);''')

t_info = conn.execute("PRAGMA table_info('Students');")

for x in t_info.fetchall():
    print(x)

conn.close()
