#!/usr/bin/env python3
# Written by Dylan Hayes

def display_menu():
    print("Monthly Sales prgram")
    print()    
    print("COMMAND MENU")
    print("view - View sales for specified month")
    print("edit - Edit sales for specified month")
    print("totals - View sales summary for year")
    print("exit - Exit program")
    print()

def main():
    display_menu()
    filename = "monthly_sales.txt"
    
    months = get_months_from_file(filename)
    three_months = get_months(months)
    view_month_count(three_months)

    while True:        
        command = input("Command: ")
        if command.lower() == "view":
            view_month_count(months)   
        elif command.lower() == "edit":
            edit(months)
        elif command.lower() == "totals":
            totals(months)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")

    print("Bye!")

def get_months_from_file(filename):
    with open(filename) as file:
        text = file.read()

def get_months(months):
    # define a dict to store the word count
    three_months = {}
    for month in months:
        if month in three_months:
            three_months[month] += 1  # increment count for word
        else:
            three_months[month] = 1   # add word with count of 1
    return three_months

def view_month_count(months):
    months = list(three_months.keys())
    months.sort(key=str.lower)
    for month in months:
        count = three_months[month]
        print(month, "=", count)

if __name__ == "__main__":
    main()
