# Dylan Hayes
# AIST 2120, PA 4 Ch. 10
#! Python 3
# 3/29/2023

print()
print('--------------------------------'.center(60))
print('---        AIST 2120         ---'.center(60))
print('---   Pgm. Assgn. 4: Regexinator Plus      ---'.center(60))
print('---    By Dylan Hayes   ---'.center(60))
print('--------------------------------'.center(60))
print()

import os
import re
import sys

# Welcome message
print("*** Welcome to Regexinator Plus ***")

# Change working directory to PA4 on Desktop
os.chdir(os.path.join(os.path.expanduser("~"), "Desktop", "PA4"))

# Prompt for input and output file names
input_file = input("Enter the name of the input file (include .txt extension): ")
output_file = input("Enter the name of the output file (include .txt extension): ")

# Read input file contents
with open(input_file, "r") as f:
    contents = f.read()

# Define regular expressions
phone_regex = re.compile(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}")
email_regex = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
date_regex = re.compile(r"\b\d{1,2}/\d{1,2}/\d{4}\b")

# Find matches for each regular expression
phone_matches = sorted(phone_regex.findall(contents))
email_matches = sorted(email_regex.findall(contents))
date_matches = sorted(date_regex.findall(contents))

# Print phone numbers to screen
print("\nHarvested Phone Numbers:")
if phone_matches:
    for match in phone_matches:
        formatted_match = re.sub(r"^(\d{3})([-.\s]?)(\d{3})([-.\s]?)(\d{4})", r"(\1)-\3-\5", match)
        print(formatted_match)
else:
    print("No matches found.")

# Print email addresses to screen
print("\nHarvested Email Addresses:")
if email_matches:
    for match in email_matches:
        print(match)
else:
    print("No matches found.")

# Print dates to screen
print("\nHarvested Dates:")
if date_matches:
    for match in date_matches:
        print(match)
else:
    print("No matches found.")

# Write results to output file if matches were found
if phone_matches or email_matches or date_matches:
    with open(output_file, "w") as f:
        f.write("Harvested Phone Numbers:\n")
        f.write("\n".join([re.sub(r"^(\d{3})", r"(\1)", match) for match in phone_matches]) + "\n\n")
        f.write("Harvested Email Addresses:\n")
        f.write("\n".join(email_matches) + "\n\n")
        f.write("Harvested Dates:\n")
        f.write("\n".join(date_matches) + "\n")
    print(f"\nResults written to {output_file}.")
else:
    print("\nNo matches found.")

# Clean program exit
sys.exit(0)

print()
print('--------------------------------'.center(60))
print('---    End Programming Assignment 4    ---'.center(60))
print('--------------------------------'.center(60))
