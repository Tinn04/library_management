import item
import borrow
import event
import volunteer
import employee

def show_menu():
    print("\nWhat would you like to do?")
    print("1. Find an item in the library")
    print("2. Borrow an item from the library")
    print("3. Return a borrowed item")
    print("4. Donate an item to the library")
    print("5. Find an event in the library")
    print("6. Register for an event in the library")
    print("7. Volunteer for the library")
    print("8. Ask for help from a librarian")
    print("9. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter the number of your choice: ").strip()
        if choice == "1":
            print("You selected: Find an item in the library.")
            item.searchItem()
        elif choice == "2":
            print("You selected: Borrow an item from the library.")
            borrow.borrowItem()
        elif choice == "3":
            print("You selected: Return a borrowed item.")
            borrow.returnItem()
        elif choice == "4":
            print("You selected: Donate an item to the library.")
            item.addItem()
            print("Thank you very much for your donation!")
        elif choice == "5":
            print("You selected: Find an event in the library.")
            event.searchEvent()
        elif choice == "6":
            print("You selected: Register for an event in the library.")
            event.registerForEvent()
        elif choice == "7":
            print("You selected: Volunteer for the library.")
            volunteer.volunteerForEvent()
        elif choice == "8":
            print("You selected: Ask for help from a librarian.")
            employee.helpFromLibrarian()
        elif choice == "9":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()
