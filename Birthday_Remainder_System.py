import os
import datetime

# Dictionary to store Birthday
birthdays = {}

# Function to get valid date input
def get_valid_date(prompt):
    while True:
        date_input = input(prompt)
        try:
            # Convert input to datetime.date
            valid_date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
            return valid_date
        except ValueError:
            print("⚠️  Invalid date format. Please enter date in 'YYYY-MM-DD' format.")    

# Function to add birthday
def add_birthday():
    name = input("\nEnter the name: ").lower().strip()
    if not name:
        print("⚠️ Name cannot be empty. Please try again..")
        return

    # Check if the name already exists
    if name in birthdays:
        print(f"⚠️  A birthday for {name} already exists on {birthdays[name].strftime('%Y-%m-%d')}.")
        
        # Handle invalid input for overwrite option
        while True:
            overwrite = input("Do you want to overwrite it? (y/n): ").strip().lower()
            if overwrite == "y":
                break
            elif overwrite == "n":
                print("👍 Keeping the existing birthday.")
                return
            else:
                print("⚠️  Invalid input...")

    # Get the valid date
    date = get_valid_date("Enter the birthday (YYYY-MM-DD) : ")
    
    # Add or update the birthday
    birthdays[name] = date
    print(f"✅ Birthday for {name} added successfully!")                

# Function to remove birthday
def remove_birthday():
    name = input("Enter name to remove: ").strip()
    if name in birthdays:
        del birthdays[name] 
        print(f"✅  Birthday for {name} removed successfully!")
    else:
        print(f"⚠️ No birthday found for {name}.")       

# Function to check upcoming birthday
def check_upcoming_birthday():
    today = datetime.date.today()
    upcoming_birthdays = []
    
    for name, date in birthdays.items():
        birthday_this_year = date.replace(year=today.year)
        days_until_birthday = (birthday_this_year - today).days
        if 0 <= days_until_birthday <= 10:
            upcoming_birthdays.append((name, date))
    
    if upcoming_birthdays:
        print("\n📅 Upcoming birthdays in next 10 days:")

        for name, date in upcoming_birthdays:
            print(f"-{name}: {date.strftime("%Y-%m-%d")}")
    else:
        print("⚠️  No upcoming birthdays in next 10 days.")

# Function to show all birthdays
def show_all():
    if birthdays:
        print("\n📅 All birthdays:")
        for name, date in sorted(birthdays.items()):
            print(f"-{name}: {date.strftime("%Y-%m-%d")}")
    else:
        print("⚠️  No birthdays found.")

# Function to search for birthday:
def search_birthday():
    name = input("Enter the name to search for: ").strip()
    if name in birthdays:
        print(f"{name}'s birthday is on {birthdays[name].strftime('%Y-%m-%d')}")
    else:
        print(f"⚠️ No birthday found for {name}.")

# Function to export birthdays to a file
def export_birthdays():
    file_name = input("Enter the file name (e.g., birthdays.txt) : ").strip()
    if file_name is not endswith("txt"):
        print("⚠️ File name must ends with '.txt'")
        return
    if not file_name:
        print("⚠️ File name cannnot be empty. Try again..")
        return
    with open*(file_name, "w") as f:
        for name, date in birthdays.items():
            f.write(f"-{name}: {date.strftime("%Y-%m-%d")}\n")
    print(f"✅  Birthdays exported to {file_name} successfully!")

# Main Program Loop
def main():
    os.system("cls")
    print("\n✨ Welcome to the Birthday Reminder System ✨")

    while True:
        print("\n" + "-" * 40)
        print("📋 MENU:")
        print("1️⃣  Add Birthday")
        print("2️⃣  Remove Birthday")
        print("3️⃣  Check upcoming Birthdays")
        print("4️⃣  Show all Birthdays")
        print("5️⃣  Search for a Birthday")
        print("6️⃣  Export Birthdays to File")
        print("7️⃣  Exit")
        print("-" * 40)


        # Prompt the user for input
        choice = input("🔷 Choose an option (1-7): ").strip()

        try:
            if choice == "1":
                add_birthday()
            elif choice == "2":
                remove_birthday()
            elif choice == "3":
                check_upcoming_birthday()
            elif choice == "4":
                show_all()
            elif choice == "5":
                search_birthday()
            elif choice == "6":
                export_birthdays()
            elif choice == "7":
                confirm_exit = input("❓ Are you sure you want to exit? (y/n): ").strip().lower()
                if confirm_exit == "y":
                    print("\n👋 Exiting the Birthday Reminder System. Goodbye!")
                    break
                else:
                    print("\n👍 Returning to the menu...")
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
        
        except Exception as e:
            print(f"⚠️  An error occurred: {e}")
            print("Returning to the main menu...")

if __name__ == "__main__":
    main()
