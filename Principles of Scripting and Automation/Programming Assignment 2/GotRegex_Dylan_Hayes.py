# Dylan Hayes
# AIST 2120, PA 1 – Ch. 3 
#! Python 3
# 3/02/2023

print()
print('--------------------------------'.center(60))
print('---        AIST 2120         ---'.center(60))
print('---   Pgm. Assgn. 2: GOT REGEX      ---'.center(60))
print('---    By Dylan Hayes   ---'.center(60))
print('--------------------------------'.center(60))
print()

print('***** MOUNTIAN DOGS EMPLOYEE EMERGENCY CONTACT LIST *****'.center(60))
print('\nThis report contains employee emergency contact information obtained from HR data.'.center(60))

print('\n~~~Report Started~~~' + "\n".center(60))

import re
import pyperclip
import sys

# Get data from clipboard
data = pyperclip.paste()

# Parse file for names, phone numbers, and dates
name_regex = r"([A-Z][a-z]+(?: [A-Z][a-z]+)?)"
phone_regex = r"(\d{3}-\d{3}-\d{4}(?: ext. \d{1,2})?|\d{3}\.\d{3}\.\d{4}|\d{3}-\d{4}(?: ext. \d)?)"
date_regex = r"(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})"

# Searches the data for all occurrences in the pattern 
matches = re.findall(f"{name_regex}.*?{phone_regex}.*?{date_regex}", data, re.DOTALL)

# Calculate the width of each column
name_width = max(len(match[0]) for match in matches)
phone_width = max(len(match[1]) for match in matches)
date_width = max(len(match[2]) for match in matches)

# Displays contact information
if not matches:
    print("No employee contact information was found. There may be a problem with the file.")
else:
    # Displays contact information
    output = ""
    
    for match in matches:
        name = match[0].ljust(name_width)
        phone = match[1].ljust(phone_width)
        date = match[2].ljust(date_width)
        output += f"{name} {phone} {date}\n"

    # Copy output to clipboard
    pyperclip.copy(output)

    print(output)
    
    print('~~~Report Complete~~~')
    
sys.exit()


print()
print()
print('--------------------------------'.center(60))
print('---    End Programming Assignment 2    ---'.center(60))
print('--------------------------------'.center(60))




