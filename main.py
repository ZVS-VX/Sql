import sqlite3
import time

with sqlite3.connect("data.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS logindata(
    id integer PRIMARY KEY,
    name text,
    surname text,
    login text,
    password blob)""")

m = input("mode 1 reg 2 log 3 look ")
match m:
    case "1":
        name = input("name: ")
        surname = input("surname: ")
        login = input("login: ")
        password = input("password: ")
        cursor.execute(f"""INSERT INTO logindata(name, surname, login, password)
         VALUES(?, ?, ?, ?)""", (name, surname, login, password))
        db.commit()
        print("Registry completed!")
        time.sleep(2)
    case "2":
        login = input("login: ")
        password = input("password: ")
        cursor.execute(f"SELECT * FROM logindata WHERE login = '{login}'")
        cf = cursor.fetchall()
        if cf:
            if cf[0][4] == password:
                print(f"Hi, {cf[0][1]} {cf[0][2]}!")
                m = input("Select mode:\n1) Quit\n2) Edit password\n3) Delete account\n")
                match m:
                    case "1":
                        print("ok")
                        time.sleep(0.3)
                    case "2":
                        oldpass = input("Write old password\n")
                        if oldpass == cf[0][4]:
                            newpass = input("Write new password\n")
                            cursor.execute(f"UPDATE logindata SET password = '{newpass}' WHERE id={cf[0][0]}")
                            db.commit()
                            print("Password edited!")
                            time.sleep(2)
                        else:
                            print("Invalid password!")
                            time.sleep(1)
                    case "3":
                        cursor.execute(f"DELETE FROM logindata WHERE id={cf[0][0]}")
                        db.commit()
                        print("Account deleted!")
                        time.sleep(2)
                    case _:
                        print("Invalid mode!")
                        time.sleep(1)

            else:
                print("Invalid password!")
                time.sleep(1)
        else:
            print("Invalid login!")
            time.sleep(1)
    case "3":
        cursor.execute("SELECT * FROM logindata ORDER BY id")
        for x in cursor.fetchall():
            print(x)
        time.sleep(7)
db.close()