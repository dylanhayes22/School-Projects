# Written by Dylan Hayes

import convert

def title():
    print("Feet and Meters Converter")
    print()

def main():
    title()
    choice = "y"
    while choice.lower() == "y":
        menu()
        number = input("Select a conversion (a/b): ")
        print()
        if number.lower() == "a":
            f = int(input("Enter Feet: "))
            c = convert.convert_feets(f)
            c = round(c, 2)
            print(c, "meters")
        elif number.lower() == "b":
            m = int(input("Enter Meters: "))
            c = convert.convert_meters(m)
            c = round(c, 2)
            print(c, "feet")
        else:
            print("Please pick a valid ")
        print()
        choice = input("Would you like to perform another conversion? (y/n): ")
        print()
    print("Thanks, Bye!")

def menu():
    print("Conversions Menu:")
    print("a. Feet to Meters")
    print("b. Meters to Feet")
    
if __name__ == "__main__":
    main()