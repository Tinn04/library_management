import sqlite3

conn = sqlite3.connect('library.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE User (
    userID INTEGER PRIMARY KEY,
    firstName TEXT NOT NULL,
    lastName TEXT NOT NULL,
    email TEXT UNIQUE,
    phone TEXT,
    membershipDate TEXT,
    category TEXT
);
''')

cursor.execute('''
CREATE TABLE Item (
    itemID INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    format TEXT,
    author TEXT,
    publisher TEXT,
    publishDate TEXT,
    status TEXT
);
''')

cursor.execute('''
CREATE TABLE Borrow (
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

conn.commit()
conn.close()
