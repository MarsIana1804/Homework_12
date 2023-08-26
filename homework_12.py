import json

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        self.contacts.append(Contact(name, phone))

    def save_to_disk(self, filename):
        data = [{"name": contact.name, "phone": contact.phone} for contact in self.contacts]
        with open(filename, "w") as file:
            json.dump(data, file)

    def load_from_disk(self, filename):
        with open(filename, "r") as file:
            data = json.load(file)
            
            self.contacts = [Contact(entry["name"], entry["phone"]) for entry in data]

    def find_by_part(self, search_string):
        findings = []

        for contact in self.contacts:
            print(contact.name, contact.phone)
            if contact.phone.find(search_string) != -1 or contact.name.find(search_string) != -1:
                findings.append(contact)
    
        return findings




address_book = AddressBook()
address_book.load_from_disk("contactlist.json")
# address_book.add_contact("John Doe", "123-456-7890")
# address_book.add_contact("Jane Smith", "987-654-3210")
for el in address_book.find_by_part("Sm"):
    print(el.phone, el.name)

address_book.save_to_disk("contactlist.json")





