from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class Name(Field):
    pass


class Phone:
    def __init__(self, name, phone=None):
        self.name = name
        self.phones = [phone] if phone else []



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

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            print(f"Invalid input: KeyError '{e.args[0]}'")
        except ValueError as e:
            print(f"Invalid input: ValueError '{e.args[0]}'")
        except IndexError as e:
            print(f"Invalid input: IndexError '{e.args[0]}'")
    return inner

@input_error
def add_contact():
    name_value = input("Enter name: ")
    name = Name(name_value)
    phone_value = input("Enter phone: ")
    phone = Phone(phone_value)
    record = Record(name)
    record.add_phone(phone)
    address_book.add_record(record)
    print(f"Contact {str(name)} with phone {str(phone)} has been added.")

@input_error
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


@input_error
def show_phone():
    name_value = input("Enter name: ")
    name = Name(name_value)
    record = address_book.data.get(str(name))
    if not record:
        print("Contact not found.")
        return
    print(f"{str(name)}: {str(record.phones[0])}")
    
    
@input_error
def remove_contact():
    name_value = input("Enter name: ")
    name = Name(name_value)
    if str(name) in address_book.data:
        del address_book.data[str(name)]
        print(f"Contact {str(name)} has been removed.")
    else:
        print("Contact not found.")


@input_error
def give_me_all():
    query = input("Enter remove: ")
    records = address_book.find_record(query)
    if not records:
        print("No matching contacts found.")
    else:
        for record in records:
            print(record)
            
            
            
def handler(command):
    if command.startswith("add"):  
            add_contact()
    elif command.startswith("change"):
            change_contact()
    elif command.startswith("phone"):
        show_phone()
    elif command.startswith("show all"):
        give_me_all()
    else:
        print("Input error: Invalid command. Please try again.")

bye = ["good bye", "close", "exit"]
hel = ["hi","hello"]


address_book = AddressBook()

def primitive_bot():
    while True:
        action = input("Welcome app to start work enter <hello> or <hi>\nTo finish, enter > (good bye, close, exit):" ).lower()
        if action in hel:
            print("How can I help you?\nThe following commands are available to you,\n(add, change, phone, remove, find, exit)")    
        elif action in bye:
            print("Good bye!")
            break
        else:
            handler(action)

if __name__ == "__main__":
    primitive_bot()
    
       
   
