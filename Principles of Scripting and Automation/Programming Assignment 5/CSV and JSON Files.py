# Dylan Hayes
# AIST 2120: Programming Assignment 5
# 04/26/2023

print()
print('--------------------------------'.center(60))
print('---        AIST 2120         ---'.center(60))
print('---   Pgm. Assgn. 5: CSV and JSON Files      ---'.center(60))
print('---    By Dylan Hayes   ---'.center(60))
print('--------------------------------'.center(60))
print()

import os
import csv
import json
import datetime
import sys

#Change the current working directory to the Desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
os.chdir(desktop_path)

#Create a new CSV file called CurrentEmpList
csv_filename = "CurrentEmpList.csv"

# 3. Read the provided file, process it, and write to the CSV file
with open("WVDogsNewHires.txt", "r") as new_hires_file, open(csv_filename, "w", newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    header = ["Employee Name", "Job Title"]
    csv_writer.writerow(header)

    for line in new_hires_file:
        line = line.strip()
        if line and "\t" in line and not line.startswith("NAME"):
            name, title = line.split("\t", maxsplit=1)
            title = title.strip()  # Remove leading and trailing whitespace from the title
            csv_writer.writerow([name, title])

#Read the data from CurrentEmpList and print it to the screen
with open(csv_filename, "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)

#Store the date that the newly created CurrentEmpList was written
json_filename = "CurrentEmpList_Date.json"
today = datetime.datetime.now()
date_dict = {"Month": today.strftime("%B"), "Day": today.day, "Year": today.year}

with open(json_filename, "w") as json_file:
    json.dump(date_dict, json_file)

print("\nThe JSON date file has been written")
formatted_date = f"{date_dict['Month']}/{date_dict['Day']}/{date_dict['Year']}"
print(f"\tIt should contain {formatted_date}")

sys.exit

print()
print('--------------------------------'.center(60))
print('---    End Programming Assignment 5    ---'.center(60))
print('--------------------------------'.center(60))
