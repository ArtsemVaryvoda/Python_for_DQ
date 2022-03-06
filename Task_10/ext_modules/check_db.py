import sqlite3
db_path = "C:\git\Python_for_DQ\Python_for_DQ\Task_10\module10.db"
conn = sqlite3.connect(db_path)
x = conn.execute('SELECT * FROM news UNION SELECT * FROM privatead UNION SELECT * FROM congratulations').fetchall()
for i in x:
    print(i)
