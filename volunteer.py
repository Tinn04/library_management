import sqlite3

def getConnection():
    return sqlite3.connect("library.db")

def volunteerForEvent():
    conn = getConnection()
    cursor = conn.cursor()

    # Asks the user for the necessary information to create a Volunteer entry
    userID = input("Enter your User ID: ").strip()
    eventID = input("Enter your Event ID: ").strip()
    role = input("Enter your role (Helper, Leader, Guide, Translator, etc): ").strip()

    if not userID.isdigit() or not eventID.isdigit():
        print("Error: User ID and Event ID must be numbers.")
        conn.close()
        return

    # Check if user is already volunteering for this event
    cursor.execute("SELECT * FROM Volunteer WHERE userID = ? AND eventID = ?", (userID, eventID))
    if cursor.fetchone():
        print("You are already registered as a volunteer for this event")
        conn.close()
        return
    
    cursor.execute(
            "INSERT INTO Volunteer (userID, eventID, role) VALUES (?, ?, ?)",
            (userID, eventID, role))
    conn.commit()
    cursor.execute("SELECT title FROM Event WHERE eventID = ?", (eventID,))
    event = cursor.fetchone()
    eventName = event[0]
    cursor.execute("SELECT firstName, lastName FROM User WHERE userID = ?", (userID,))
    user = cursor.fetchone()
    userFirstName, userLastName = user

    print(f"Successfully registered {userFirstName} {userLastName} as a volunteer ({role}) for the event, {eventName}")