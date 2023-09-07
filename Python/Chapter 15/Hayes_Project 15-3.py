#!/usr/bin/env python3
# Written by Dylan Hayes

class Person:
    def  __init__(self, first_name, last_name, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        
    @classmethod
    def user_input(self):
        while 1:
            #try:
                first_name = input("First name: ")
                last_name = input("Last name: ")
                email_address = input("Email : ")
                return self(first_name, last_name, email_address)
            #except:
            #    print("Invalid Input")
            #    continue
            
class Customer(Person):
    def __init__(self, first_name, last_name, email_address, number):
        Person.__init__(self, first_name, last_name, email_address)
        self.number = number
        
        def user_input(self):
            while 1:
                try:
                    first_name = input("First name: ")
                    last_name = input("Last name: ")
                    email_address = input("Email : ")
                    number = input("Number: ")
                    return self(first_name, last_name, email_address, number)
                except:
                    print("Invalid Input")
                    continue

class Employee(Person):
    def __init__(self, first_name, last_name, email_address):
        super().__init__(first_name, last_name, email_address)
        self.ssn = input("SSN: ")
        return self(ssn)

def main():
    print("Customer/Employee Data Entry")
    print()
    
    person = Customer.user_input
    first_name = Person.user_input
    last_name = Person.user_input
    email_address = Person.user_input
    number  = Customer.user_input
    
    choice = "y"
    while choice.lower() == "y":
        pick = input("Customer or employee? (c/e): ")
        if pick == "c":

            Customer(first_name, last_name, email_address, number)
        elif pick == "e":
            print("d")
 
        Customers= Customer.user_input()
        persons = Person.user_input()
        print()
        choice = input("Continue? (y/n): ")
    print("Bye!")
    print()
    
if __name__ == "__main__":
    main()

