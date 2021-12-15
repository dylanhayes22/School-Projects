#!/usr/bin/env python3
# Written by Dylan Hayes

def display_menu():
    print("Contact Manager")
    print()
    print("COMMAND MENU")
    print("list - List all ccontacts")
    print("view - View a contact")
    print("add  - Add a contact")
    print("del  - Delete a contacts")
    print("exit - Exit program")
    print()

def list(contact_list):
    if len(contact_list) == 0:
        print("There are no movies in the list.\n")
        return
    else:
        i = 1
        for row in contact_list:
            print(str(i) + ". " + row[0])
            i += 1
        print()
        
def view(contact_list):
    number = int(input("Number: "))
    if number < 1 or number > len(contact_list):
        print("Invalid contact number.\n")
    else:
        number = int(number)
        contact = contact_list[number-1]
        print('Name: {0}\nEmail: {1}\nPhone: {2}'.format(*contact))
        print()

def add(contact_list):
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    contact = []
    contact.append(name)
    contact.append(email)
    contact.append(phone)
    contact_list.append(contact)
    print(contact[0] + " was added.\n")
    print()

def delete(contact_list):
    number = int(input("Number: "))
    if number < 1 or number > len(contact_list):
        print("Invalid contact number.\n")
    else:
        contact = contact_list.pop(number-1)
        print(contact[0] + " was deleted.\n")
        print()

def main():
    contact_list = [["Guido van Rossum", ],
                    ["Eric Idle", "eric@ericidle.com", "+44 20 7976 0958"]]
    display_menu()

    while True:        
        command = input("Command: ")
        if command.lower() == "list":
            list(contact_list)   
        elif command.lower() == "view":
            view(contact_list)
        elif command.lower() == "add":
            add(contact_list)
        elif command.lower() == "del":
            delete(contact_list)  
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")

    print("Bye!")

if __name__ == "__main__":
    main()
