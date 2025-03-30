import sqlite3

def getConnection():
    return sqlite3.connect("library.db")

def borrowItem():
    conn = getConnection()
    cursor = conn.cursor()

    itemID = input("Enter the itemID you want to borrow: ")
    cursor.execute("SELECT status FROM Item WHERE itemID = ?", (itemID,))
    result = cursor.fetchone()

    if not result:
        print("Item not found")
    elif result[0] != "Available":
        print("This item is not available for borrowing")
    else:
        userID = input("Enter your userID: ")
        borrowDate = ("Enter today's date(YYYY-MM-DD): ")
        dueDate = input("Enter due date (YYYY-MM-DD): ")

        # Get next borrowID
        cursor.execute("SELECT MAX(borrowID) FROM Borrow")
        previousID = cursor.fetchone()[0]
        newID = 1 if previousID is None else previousID + 1

        cursor.execute("""
            INSERT INTO Borrow(borrowID, userID, itemID, borrowDate, dueDate, returnDate, fineAmount)
            VALUES (?, ?, ?, ?, ?, NULL, 0.0)
        """, (newID, userID, itemID, borrowDate, dueDate))
        conn.commit()
        print("Item successfully borrowed.")
    conn.close()

def returnItem():
    conn = getConnection()
    cursor = conn.cursor()

    itemID = input("Enter the itemID to return: ")
    cursor.execute("SELECT status FROM Item WHERE itemID = ?", (itemID,))
    result = cursor.fetchone()
    
    if not result:
        print("Item not found.")
    elif result[0] == "Available":
        print("This item is already marked as available.")
    else:
        confirm = input("Type 'CONFIRM' to return the item or 'EXIT' to cancel: ")
        if confirm.upper() == "CONFIRM":
            returnDate = input("Enter today's date: ")
            cursor.execute("""
                UPDATE Borrow
                SET returnDate = ?
                WHERE itemID = ? AND returnDate IS NULL
            """, (returnDate, itemID))
            conn.commit()
            print("Item successfully returned.")
        else:
            print("Return cancelled.")