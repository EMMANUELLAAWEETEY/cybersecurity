# Simple Contact Book

CONTACT_FILE = "contacts.txt"

# Function to add a contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    with open(CONTACT_FILE, "a") as file:
        file.write(f"{name},{phone}\n")

    print("✅ Contact added successfully!\n")

# Function to view all contacts
def view_contacts():
    try:
        with open(CONTACT_FILE, "r") as file:
            contacts = file.readlines()

        if not contacts:
            print("⚠️ No contacts found.\n")
        else:
            print("\n📒 Contact List:")
            for contact in contacts:
                name, phone = contact.strip().split(",")
                print(f"- {name} : {phone}")
            print()
    except FileNotFoundError:
        print("⚠️ No contact file found. Add a contact first.\n")

# Function to delete a contact
def delete_contact():
    name_to_delete = input("Enter the name of the contact to delete: ")

    try:
        with open(CONTACT_FILE, "r") as file:
            contacts = file.readlines()

        with open(CONTACT_FILE, "w") as file:
            found = False
            for contact in contacts:
                name, phone = contact.strip().split(",")
                if name.lower() != name_to_delete.lower():
                    file.write(contact)
                else:
                    found = True

        if found:
            print("🗑️ Contact deleted successfully!\n")
        else:
            print("❌ Contact not found.\n")

    except FileNotFoundError:
        print("⚠️ No contact file found.\n")

# Main menu
def main():
    while True:
        print("===== CONTACT BOOK =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice! Try again.\n")

# Run the program
if __name__ == "__main__":
    main()
