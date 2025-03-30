import sqlite3

conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# Creating table for User
cursor.execute('''
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
cursor.execute('''
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
cursor.execute('''
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
cursor.execute("""
CREATE TABLE IF NOT EXISTS Event (
    EventID INTEGER PRIMARY KEY,
    Title TEXT,
    Type TEXT,
    Description TEXT,
    TargetAudience TEXT,
    Date TEXT,
    StartTime TEXT,
    EndTime TEXT,
    RoomID INTEGER,
    FOREIGN KEY (RoomID) REFERENCES Room(RoomID)
);
""")

# Creating table for Room
cursor.execute("""
CREATE TABLE IF NOT EXISTS Room (
    RoomID INTEGER PRIMARY KEY,
    RoomName TEXT,
    Capacity INTEGER
);
""")

# Creating table for Attendance
cursor.execute("""
CREATE TABLE IF NOT EXISTS Attendance (
    EventID INTEGER,
    UserID INTEGER,
    PRIMARY KEY (EventID, UserID),
    FOREIGN KEY (EventID) REFERENCES Event(EventID),
    FOREIGN KEY (UserID) REFERENCES User(UserID)
);
""")

# Creating table for Employee
cursor.execute("""
CREATE TABLE IF NOT EXISTS Employee (
    EmployeeID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Role TEXT,
    HireDate TEXT,
    Email TEXT,
    Phone TEXT
);
""")

# Creating trigger to prevent the borrowing of unavailable items
cursor.execute("""
CREATE TRIGGER prevent_unavailable_borrow
BEFORE INSERT ON Borrow
FOR EACH ROW
WHEN (SELECT Status FROM Item WHERE ItemID = NEW.ItemID) != 'Available'
BEGIN
    SELECT RAISE(ABORT, 'Item is not available for borrowing.');
END;
""")

# Creating trigger to automatically update the status to "Borrowed" when an item is being borrowed
cursor.execute("""
CREATE TRIGGER update_item_status_on_borrow
AFTER INSERT ON Borrow
FOR EACH ROW
BEGIN
    UPDATE Item SET Status = 'Borrowed' WHERE ItemID = NEW.ItemID;
END;
""")

# Creating trigger to automatically update the status to "Available" when an item is returned
cursor.execute("""
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
