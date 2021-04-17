import sqlite3


def list_employees(cur):
    print("Employees")
    print("=" * 20)
    cur.execute("select * from employees")
    for id, name, job, salary in cur.fetchall():
        print(f"{id:5} {name:30} {job:10} {salary:10}")

    print("=" * 50)


def add_employee(con, cur):
    name = input("Enter name :")
    job = input("Enter job :")
    salary = int(input("Enter salary :"))
    try:
        cur.execute("insert into employees(fullname,job,salary) values(?,?,?)",
                    (name, job, salary))
        print("Added Employee Successfully!")
        con.commit()  # Commit Transaction
    except Exception as ex:
        print("Error : ", ex)


def update_employee(con, cur):
    pass


def delete_employee(con, cur):
    pass


con = sqlite3.connect(r"d:\classroom\mar2\hr.db")
cur = con.cursor()

while True:
    print("\nEmployees Menu")
    print("1. List Employees")
    print("2. Add Employee")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")
    choice = int(input("Enter choice [1-5] :"))
    if choice == 1:
        list_employees(cur)
    elif choice == 2:
        add_employee(con, cur)
    elif choice == 5:
        break

cur.close()
con.close()
