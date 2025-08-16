class ContactBook:
    def __init__(self, filename="contacts.txt"):
        self.filename = filename

    def add_contact(self, name, phone):
        try:
            with open(self.filename, "a") as f:
                f.write(f"{name},{phone}\n")
            print("Contact added.")
        except Exception as e:
            print("Error:", e)

    def display_contact(self, name, phone):
        print(f"Name: {name} | Phone: {phone}")

    def view_contacts(self):
        try:
            with open(self.filename, "r") as f:
                lines = f.readlines()
            if not lines:
                print("No contacts found.")
                return
            print("\nAll Contacts:")
            for line in lines:
                name, phone = line.strip().split(",")
                self.display_contact(name, phone)
        except FileNotFoundError:
            print("No contact file found. Add a contact first.")

    def search_contact(self, search_term):
        try:
            with open(self.filename, "r") as f:
                lines = f.readlines()
            matches = [line.strip().split(",") for line in lines if search_term.lower() in line.lower()]
            if matches:
                print("\nSearch Results:")
                for name, phone in matches:
                    self.display_contact(name, phone)
            else:
                print("No matching contact.")
        except FileNotFoundError:
            print("No contact file found. Add a contact first.")

    def menu(self):
        while True:
            print("\n=== Contact Book ===")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Exit")
            choice = input("Choose (1-4): ").strip()

            if choice == "1":
                name = input("Enter name: ").strip()
                phone = input("Enter phone: ").strip()
                self.add_contact(name, phone)
            elif choice == "2":
                self.view_contacts()
            elif choice == "3":
                search_term = input("Enter name to search: ").strip()
                self.search_contact(search_term)
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1-4.")
if __name__ == "__main__":
    cb = ContactBook()
    cb.menu()