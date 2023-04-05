from collections import UserDict


class Name:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class Phone:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class Record:
    def __init__(self, name):
        self.name = name
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)

    def remove_phone(self, phone):
        self.phones.remove(phone)

    def edit_phone(self, phone, new_phone):
        index = self.phones.index(phone)
        self.phones[index] = new_phone

    def __str__(self):
        return f"{str(self.name)}: {', '.join(str(phone) for phone in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[str(record.name)] = record

    def remove_record(self, name):
        del self.data[str(name)]

    def find_record(self, query):
        result = []
        for record in self.data.values():
            if query.lower() in str(record).lower():
                result.append(record)
        return result


def add_contact():
    name_value = input("Enter name: ")
    name = Name(name_value)
    phone_value = input("Enter phone: ")
    phone = Phone(phone_value)
    record = Record(name)
    record.add_phone(phone)
    address_book.add_record(record)
    print(f"Contact {str(name)} with phone {str(phone)} has been added.")


def change_contact():
    name_value = input("Enter name: ")
    name = Name(name_value)
    record = address_book.data.get(str(name))
    if not record:
        print("Contact not found.")
        return
    phone_value = input("Enter new phone: ")
    phone = Phone(phone_value)
    record.edit_phone(record.phones[0], phone)
    print(f"Phone for contact {str(name)} has been changed to {str(phone)}.")


def show_phone():
    name_value = input("Enter name: ")
    name = Name(name_value)
    record = address_book.data.get(str(name))
    if not record:
        print("Contact not found.")
        return
    print(f"{str(name)}: {str(record.phones[0])}")


def give_me_all():
    query = input("Enter query: ")
    records = address_book.find_record(query)
    if not records:
        print("No matching contacts found.")
    else:
        for record in records:
            print(record)

bye = ["good bye", "close", "exit"]
hel = ["hi","hello"]

address_book = AddressBook()
while True:
    action = input("Welcome app >>> action: (add, change, phone, find, exit): ").lower()
    if action in hel:
        print("How can I help you?")
    elif action == "add":
        add_contact()
    elif action == "change":
        change_contact()
    elif action == "phone":
        show_phone()
    elif action == "find":
        give_me_all()
    elif action in bye:
        break
   