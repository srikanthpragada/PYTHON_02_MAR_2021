import sqlite3

con = sqlite3.connect(r"d:\classroom\mar2\hr.db")
cur = con.cursor()
cur.execute("select * from employees")
for id, name, job, salary in cur.fetchall():
    print(f"{id:5} {name:30} {job:10} {salary:10}")

cur.close()
con.close()
