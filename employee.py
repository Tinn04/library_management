import sqlite3
import random
import time

def getConnection():
    return sqlite3.connect("library.db")

def helpFromLibrarian():
    conn = getConnection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT firstName, lastName FROM Employee")
    employees = cursor.fetchall()

    randomEmployee = random.choice(employees)
    print(f"\n{randomEmployee[0]} {randomEmployee[1]} will help you.")
    time.sleep(random.randint(2, 4))
    print(f"{randomEmployee[0]} {randomEmployee[1]}: Hello! That is beyond my scope. I will escalate your case to the regional manager")
    time.sleep(3)
    print(f"{randomEmployee[0]} {randomEmployee[1]}: Have a good day!")
    time.sleep(1)
    conn.close()