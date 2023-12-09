import json

class ContactManager:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def save_contacts(self):
        with open(self.filename, "w") as file:
            json.dump(self.contacts, file, indent=2)

    def add_contact(self, name, phone, email, address):
        contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }
        self.contacts.append(contact)
        self.save_contacts()

    def view_contacts(self):
        for i in range(len(self.contacts)):
            contact = self.contacts[i]
            print(f"{i + 1}. {contact['name']} - {contact['phone']}")

    def search_contacts(self, search_term):
        results = [contact for contact in self.contacts if
                   search_term.lower() in contact["name"].lower() or search_term in contact["phone"]]
        return results

    def update_contact(self, index, name, phone, email, address):
        if 0 < index <= len(self.contacts):
            self.contacts[index - 1] = {
                "name": name,
                "phone": phone,
                "email": email,
                "address": address
            }
            self.save_contacts()
            return True
        return False

    def delete_contact(self, index):
        if 0 < index <= len(self.contacts):
            del self.contacts[index - 1]
            self.save_contacts()
            return True
        return False

def print_menu():
    print("\nContact Manager Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contacts")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def main():
    contact_manager = ContactManager()

    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter the name: ")
            phone = input("Enter the phone number: ")
            email = input("Enter the email address: ")
            address = input("Enter the address: ")
            contact_manager.add_contact(name, phone, email, address)
            print("Contact added successfully!")

        elif choice == "2":
            print("\nContact List:")
            contact_manager.view_contacts()

        elif choice == "3":
            search_term = input("Enter the name or phone number to search: ")
            results = contact_manager.search_contacts(search_term)
            if results:
                print("\nSearch Results:")
                for i in range(len(results)):
                    contact = results[i]
                    print(f"{i + 1}. {contact['name']} - {contact['phone']}")
            else:
                print("No matching contacts found.")

        elif choice == "4":
            index = int(input("Enter the index of the contact to update: "))
            name = input("Enter the updated name: ")
            phone = input("Enter the updated phone number: ")
            email = input("Enter the updated email address: ")
            address = input("Enter the updated address: ")
            if contact_manager.update_contact(index, name, phone, email, address):
                print("Contact updated successfully!")
            else:
                print("Invalid index.")

        elif choice == "5":
            index = int(input("Enter the index of the contact to delete: "))
            if contact_manager.delete_contact(index):
                print("Contact deleted successfully!")
            else:
                print("Invalid index.")

        elif choice == "6":
            print("Exiting the Contact Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
