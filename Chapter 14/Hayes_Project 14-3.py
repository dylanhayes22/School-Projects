#!/usr/bin/env python3
# Written by Dylan Hayes

import csv
import sys

FILENAME = "customers.csv"

def main():
    print("Customer Viewer")
    print()
    choice = "y"
    while choice.lower() == "y":
        user_num = input("Enter customer ID: ")
        if (user_num == ""):
            print("Empty input. Please enter again.")
        found = False
        with open(FILENAME) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if (row['cust_id'] == user_num):
                    print()
                    print("{0} {1}\n{2} \n{3} \n{4}, {5} {6}".format(row['first_name'],row['last_name'],row['company_name'],row['address'],row['city'],row['state'],row['zip']))
                    found = True
                    break
            if not found:
                print()
                print("No customer with that ID.")
                choice = "y"
                
        print()
        choice = input ("Continue? (y/n): ")
        print()
    print("Bye!") 
         
if __name__ == "__main__":
    main()

