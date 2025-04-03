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
    print(f"\n{randomEmployee[0]} {randomEmployee[1]} is available to help you.")
    time.sleep(2)
    print(f"\n Hello! I'm {randomEmployee[0]} {randomEmployee[1]} and I'm happy to help.")
    print(f"\n Please direct any questions you may have to my email, {randomEmployee[0]}{randomEmployee[1]}@lib.ca")
    time.sleep(2)
    conn.close()