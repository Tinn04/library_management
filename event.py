import sqlite3

def getConnection():
    return sqlite3.connect("library.db")

# Once again probably a debugging function
def displayEvents():
    conn = getConnection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT E.eventID, E.title, E.description, E.date, E.startTime, E.endTime,
               E.type, E.targetAudience, R.roomName
        FROM Event E
        JOIN Room R ON E.roomID = R.roomID
    """)
    events = cursor.fetchall()
    print("\n--- List of All Events ---")
    for event in events:
        print(f"ID: {event[0]}, Title: {event[1]}, Description: {event[2]}, Date: {event[3]}, Start Time: {event[4]}, End Time: {event[5]}, Type: {event[6]}, Target Audience: {event[7]}, Room: {event[8]}")
    conn.close()

def searchEvent():
    conn = getConnection()
    cursor = conn.cursor()

    print("\nSearch Event By:")
    print("1. Event ID")
    print("2. Event Name")
    choice = input("Enter your choice: ")

    if choice == '1':
        eventID = input("Enter Event ID: ")
        cursor.execute("""
            SELECT E.eventID, E.title, E.description, E.date, E.startTime, E.endTime,
                   E.type, E.targetAudience, R.roomName
            FROM Event E
            JOIN Room R ON E.roomID = R.roomID
            WHERE E.eventID = ?
        """, (eventID,))
        event = cursor.fetchone()
        if event:
            print(f"ID: {event[0]}, Title: {event[1]}, Description: {event[2]}, Date: {event[3]}, "
                  f"Start Time: {event[4]}, End Time: {event[5]}, Type: {event[6]}, "
                  f"Target Audience: {event[7]}, Room: {event[8]}")
        else:
            print("No event found with that ID.")
    elif choice == '2':
        name = input("Enter Event Name: ")
        cursor.execute("""
            SELECT E.eventID, E.title, E.description, E.date, E.startTime, E.endTime,
                   E.type, E.targetAudience, R.roomName
            FROM Event E
            JOIN Room R ON E.roomID = R.roomID
            WHERE E.title = ?
        """, (name,))
        matches = cursor.fetchall()
        if not matches:
            print("No events found with that name.")
        elif len(matches) == 1:
            event = matches[0]
            print(f"ID: {event[0]}, Title: {event[1]}, Description: {event[2]}, Date: {event[3]}, "
                  f"Start Time: {event[4]}, End Time: {event[5]}, Type: {event[6]}, "
                  f"Target Audience: {event[7]}, Room: {event[8]}")
        else:
            print("Multiple events found:")
            for idx, event in enumerate(matches):
                print(f"{idx + 1}. ID: {event[0]}, Title: {event[1]}, Description: {event[2]}, Date: {event[3]}, "
                      f"Start Time: {event[4]}, End Time: {event[5]}, Type: {event[6]}, "
                      f"Target Audience: {event[7]}, Room: {event[8]}")
            selection = int(input("Select the number of the event: "))
            if 1 <= selection <= len(matches):
                event = matches[selection - 1]
                print(f"Selected Event:\nID: {event[0]}, Title: {event[1]}, Description: {event[2]}, Date: {event[3]}, "
                      f"Start Time: {event[4]}, End Time: {event[5]}, Type: {event[6]}, "
                      f"Target Audience: {event[7]}, Room: {event[8]}")
            else:
                print("Invalid selection.")
    else:
        print("Invalid choice.")
    conn.close()