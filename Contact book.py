class Contact:
  def __init__(self, name, phone, email, address):
    self.name = name
    self.phone = phone
    self.email = email
    self.address = address

  def __str__(self):
    return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}\nAddress: {self.address}"

class ContactBook:
  def __init__(self):
    self.contacts = []

  def add_contact(self):
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    contact = Contact(name, phone, email, address)
    self.contacts.append(contact)
    print("Contact added successfully!")

  def view_contacts(self):
    if not self.contacts:
      print("No contacts saved yet.")
    else:
      for contact in self.contacts:
        print(contact)
        print("-" * 20)

  def search_contact(self):
    search_term = input("Enter name or phone number to search: ")
    found = False
    for contact in self.contacts:
      if search_term.lower() in contact.name.lower() or search_term in contact.phone:
        print(contact)
        found = True
        break
    if not found:
      print("Contact not found.")

  def update_contact(self):
    name = input("Enter the name of the contact to update: ")
    for i, contact in enumerate(self.contacts):
      if contact.name.lower() == name.lower():
        print("Current details:")
        print(contact)
        new_phone = input("Enter new phone number (leave blank to keep current): ")
        new_email = input("Enter new email address (leave blank to keep current): ")
        new_address = input("Enter new address (leave blank to keep current): ")
        if new_phone:
          contact.phone = new_phone
        if new_email:
          contact.email = new_email
        if new_address:
          contact.address = new_address
        self.contacts[i] = contact
        print("Contact updated successfully!")
        return
    print("Contact not found.")
  def delete_contact(self):
    name = input("Enter the name of the contact to delete: ")
    for i, contact in enumerate(self.contacts):
      if contact.name.lower() == name.lower():
        del self.contacts[i]
        print("Contact deleted successfully!")
        return
    print("Contact not found.")

def main():
  contact_book = ContactBook()
  while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
      contact_book.add_contact()
    elif choice == '2':
      contact_book.view_contacts()
    elif choice == '3':
      contact_book.search_contact()
    elif choice == '4':
      contact_book.update_contact()
    elif choice == '5':
      contact_book.delete_contact()
    elif choice == '6':
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()
