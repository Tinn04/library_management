import os
import sqlite3
import database
from userInterface import main as run_user_interface

DB_PATH = "library.db"
SQL_ENTRY_FILE = "example_entries.sql"

def runSQLScript(db_path, sql_file):
    """Run SQL script to populate database entries."""
    if not os.path.exists(sql_file):
        print(f"SQL file '{sql_file}' not found. Cmon Tin where you running this from?")
        return
    with open(sql_file, "r") as f:
        sql_script = f.read()
    conn = sqlite3.connect(db_path)
    try:
        conn.executescript(sql_script)
        print(f"Data from '{sql_file}' successfully loaded into '{db_path}'.")
    except sqlite3.Error as e:
        print(f"Error executing SQL script: {e}")
    finally:
        conn.close()

def main():
    print("Setting up the library database...")
    database.createTables()
    runSQLScript(DB_PATH, SQL_ENTRY_FILE)

    print("Database ready. Launching user interface...\n")
    run_user_interface()

if __name__ == "__main__":
    main()
