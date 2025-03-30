import sqlite3

def getConnection():
    return sqlite3.connect("library.db")

# I'm not sure if I'll ever need this function but I just added it for completion and debugging
def displayItems():
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Item")
    items = cursor.fetchall()
    
    print("\n--- List of All Items ---")
    for item in items:
        print(f"ID: {item[0]}, Title: {item[1]}, Format: {item[2]}, Author: {item[3]}, Publisher: {item[4]}, Publish Date: {item[5]}, Status: {item[6]}")
    conn.close()

def addItem():
    conn = getConnection()
    cursor = conn.cursor()

    # Gather all the necessary information
    # itemID and status will automatically be generated (assumed to be "Available" for status)
    title = input("Enter item title: ")
    format = input("Enter item format (Book, CD, etc.): ")
    author = input("Enter item author: ")
    publisher = input("Enter publisher name: ")
    publishDate = input("Enter publish date (YYYY-MM-DD): ")
    status = "Available"

    cursor.execute("SELECT MAX(itemID) FROM Item")
    previousID = cursor.fetchone()[0]
    newID = (previousID + 1) if previousID else 1

    cursor.execute("""
    INSERT INTO Item(itemID, title, format, author, publisher, publishDate, status)
    VALUES (?, ?, ?, ?, ?, ?, ?)""",
    (newID, title, format, author, publisher, publishDate, status))

    conn.commit()
    conn.close()
    print("Item added successfully with ID:", newID)

def searchItem():
    conn = getConnection()
    cursor = conn.cursor()

    print("\nSearch Item By:")
    print("1. Item ID")
    print("2. Item Name")
    choice = input("Enter your choice: ")
    if choice == "1":
        itemID = input("Enter the Item ID: ")
        cursor.execute("SELECT * FROM Item WHERE itemID = ?", (itemID,))
        item = cursor.fetchone()
        if item:
            print(f"ID: {item[0]}, Title: {item[1]}, Format: {item[2]}, Author: {item[3]}, Publisher: {item[4]}, Publish Date: {item[5]}, Status: {item[6]}")
        else:
            print("No item found with that ID.")
    
    elif choice == "2":
        title = input("Enter the item title: ")
        cursor.execute("SELECT * FROM Item WHERE title = ?", (title,))
        items = cursor.fetchall()

        if not items:
            print("No item found with that title.")
        elif len(items) == 1:
            item = items[0]
            print(f"ID: {item[0]}, Title: {item[1]}, Format: {item[2]}, Author: {item[3]}, Publisher: {item[4]}, Publish Date: {item[5]}, Status: {item[6]}")
        else:
            print("Multiple items found with that title:")
            for item in items:
                print(f"ID: {item[0]}, Author: {item[3]}, Publisher: {item[4]}, Date: {item[5]}, Status: {item[6]}")

            selected_id = input("Enter the ID of the item you want to view: ")
            cursor.execute("SELECT * FROM Item WHERE itemID = ?", (selected_id,))
            item = cursor.fetchone()
            if item:
                print(f"ID: {item[0]}, Title: {item[1]}, Format: {item[2]}, Author: {item[3]}, Publisher: {item[4]}, Publish Date: {item[5]}, Status: {item[6]}")
            else:
                print("Invalid selection.")
    
    else:
        print("Invalid choice. Please enter 1 or 2.")

    conn.close()