import sqlite3

def createTables():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    # Creating table for User
    cursor.executescript('''
    CREATE TABLE IF NOT EXISTS User (
        userID INTEGER PRIMARY KEY,
        firstName TEXT NOT NULL,
        lastName TEXT NOT NULL,
        email TEXT UNIQUE,
        phone TEXT,
        membershipDate TEXT,
        category TEXT
    );
    ''')

    # Creating table for Item
    cursor.executescript('''
    CREATE TABLE IF NOT EXISTS Item (
        itemID INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        format TEXT,
        author TEXT,
        publisher TEXT,
        publishDate TEXT,
        status TEXT
    );
    ''')

    # Creating table for Borrow
    cursor.executescript('''
    CREATE TABLE IF NOT EXISTS Borrow (
        borrowID INTEGER PRIMARY KEY,
        userID INTEGER,
        itemID INTEGER,
        borrowDate TEXT,
        dueDate TEXT,
        returnDate TEXT,
        fineAmount REAL,
        FOREIGN KEY (userID) REFERENCES User(userID),
        FOREIGN KEY (itemID) REFERENCES Item(itemID)
    );
    ''')

    # Creating table for Event
    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS Event (
        eventID INTEGER PRIMARY KEY,
        title TEXT,
        description TEXT,
        date TEXT,
        startTime TEXT,
        endTime TEXT,
        type TEXT,
        targetAudience TEXT,
        roomID INTEGER,
        FOREIGN KEY (roomID) REFERENCES Room(roomID)
    );
    """)

    # Creating table for Room
    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS Room (
        roomID INTEGER PRIMARY KEY,
        roomName TEXT,
        capacity INTEGER
    );
    """)

    # Creating table for Attendance
    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS Attendance (
        eventID INTEGER,
        userID INTEGER,
        PRIMARY KEY (eventID, userID),
        FOREIGN KEY (eventID) REFERENCES Event(eventID),
        FOREIGN KEY (userID) REFERENCES User(userID)
    );
    """)

    # Creating table for Employee
    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS Employee (
        employeeID INTEGER PRIMARY KEY,
        firstName TEXT NOT NULL,
        lastName TEXT NOT NULL,
        role TEXT,
        hireDate TEXT,
        email TEXT,
        phone TEXT
    );
    """)

    # Creating table for Volunteer
    cursor.executescript("""
    CREATE TABLE Volunteer (
        userID INTEGER,
        eventID INTEGER,
        role TEXT,
        PRIMARY KEY (userID, eventID),
        FOREIGN KEY (userID) REFERENCES User(userID),
        FOREIGN KEY (eventID) REFERENCES Event(eventID)
    );
    """)

    # Creating trigger to prevent the borrowing of unavailable items
    cursor.executescript("""
    DROP TRIGGER IF EXISTS prevent_unavailable_borrow;

    CREATE TRIGGER prevent_unavailable_borrow
    BEFORE INSERT ON Borrow
    FOR EACH ROW
    WHEN EXISTS (
        SELECT 1 FROM Item
        WHERE ItemID = NEW.ItemID AND Status != 'Available'
    )
    BEGIN
        SELECT RAISE(ABORT, 'Item is not available for borrowing.');
    END;
    """)


    # Creating trigger to automatically update the status to "Borrowed" when an item is being borrowed
    cursor.executescript("""
    DROP TRIGGER IF EXISTS update_item_status_on_borrow;
                        
    CREATE TRIGGER update_item_status_on_borrow
    AFTER INSERT ON Borrow
    FOR EACH ROW
    BEGIN
        UPDATE Item SET Status = 'Borrowed' WHERE ItemID = NEW.ItemID;
    END;
    """)

    # Creating trigger to automatically update the status to "Available" when an item is returned
    cursor.executescript("""
    DROP TRIGGER IF EXISTS update_item_status_on_return;
                        
    CREATE TRIGGER update_item_status_on_return
    AFTER UPDATE OF ReturnDate ON Borrow
    FOR EACH ROW
    WHEN NEW.ReturnDate IS NOT NULL
    BEGIN
        UPDATE Item SET Status = 'Available' WHERE ItemID = NEW.ItemID;
    END;
    """)
    conn.commit()
    conn.close()
