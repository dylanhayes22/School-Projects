#!/usr/bin/env python3
# Written by Dylan Hayes

import csv
FILENAME = "contacts.csv"

def write_contacts(contacts):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(contacts)   

def read_contacts():
    contacts = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            contacts.append(row)
    return contacts

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

def list(contacts):
    for i in range(len(contacts)):
        contact = contacts[i]
        print(str(i+1) + ". " + contact[0])
    print()
        
def view(contacts):
    number = int(input("Number: "))
    if number < 1 or number > len(contacts):
        print("Invalid contact number.\n")
    else:
        number = int(number)
        contact = contacts[number-1]
        print('Name: {0}\nEmail: {1}\nPhone: {2}'.format(*contact))
        print()

def add(contacts):
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    contact = []
    contact.append(name)
    contact.append(email)
    contact.append(phone)
    contacts.append(contact)
    write_contacts(contacts)
    print(name + " was added.\n")

def delete(contacts):
    index = int(input("Number: ")) 
    if index < 1 or index > len(contacts):
        print("Invalid contact number.\n")
    else:
        contact = contacts.pop(index - 1)
        write_contacts(contacts)
        print(contact[0] + " was deleted.\n")
          
def main():
    contacts = read_contacts()
    display_menu()

    while True:        
        command = input("Command: ")
        if command.lower() == "list":
            list(contacts)   
        elif command.lower() == "view":
            view(contacts)
        elif command.lower() == "add":
            add(contacts)
        elif command.lower() == "del":
            delete(contacts)  
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")

    print("Bye!")

if __name__ == "__main__":
    main()
