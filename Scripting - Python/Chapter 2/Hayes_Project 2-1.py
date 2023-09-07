#!/usr/bin/env python3
# Written by Dylan Hayes

import locale

# set the locale for use in currency formatting
result = locale.setlocale(locale.LC_ALL, '')
if result == "C" or result.startswith("C/"):
    locale.setlocale(locale.LC_ALL, 'en_US')

    # display a welcome message
print("Registration Form")
print()

    # get input from the user
first_name = (input("First Name:\t"))
last_name = (input("Last Name:\t"))
birth_year = (input("Birth Year:\t"))

    # store temp password and full name
temp_pass = (first_name + '*' + birth_year)

    # display temp password
print()
print('Welcome', first_name, last_name + '!')
print('Your registration is complete.')
    
print('Your temporary password is:', temp_pass)