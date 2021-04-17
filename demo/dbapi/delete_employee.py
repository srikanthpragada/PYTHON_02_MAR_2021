import sqlite3

try:
    con = sqlite3.connect(r"d:\classroom\mar2\hr.db")
    cur = con.cursor()
    try:
        id = int(input("Enter id :"))
        cur.execute("delete from employees where id = ?", (id,))
        if cur.rowcount == 1:
            print("Deleted Successfully!")
            con.commit()
        else:
            print("Sorry! Employee id not found!")
    except Exception as ex:
        print("Error : ", ex)
    finally:
        cur.close()

    con.close()
except Exception as ex:
    print("Error:" , ex)

