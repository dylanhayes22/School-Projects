# Dylan Hayes
# AIST 2120, PA 3 Ch. 9
#! Python 3
# 3/5/2023

import os
import re

print()
print('--------------------------------'.center(60))
print('---        AIST 2120         ---'.center(60))
print('---   Pgm. Assgn. 3: FUN WITH FILES      ---'.center(60))
print('---    By Dylan Hayes   ---'.center(60))
print('--------------------------------'.center(60))
print()


print('***** WEST VIRGINIA HOT DOGS CONSOLIDATES HIRING: CURRENT WEEK *****'.center(60))

# Define file names and paths
chasHr = "WVDogsChasHR.txt"
auburHr = "WVDogsAuburnHR.txt"
combinedHr = "WVDogsCombinedHiring.txt"
desktopPath = os.path.abspath(os.path.expanduser("~/Desktop"))

# Check if current directory is desktop, change if necessary
print("\nThe starting CWD is", os.getcwd())

if os.path.abspath(os.getcwd()) == desktopPath:
    print("\tCurrent directory is verified as ", os.getcwd())
else:
    print("\tHR files are on the Desktop. Changing directory to match.")
    os.chdir(desktopPath)
    print("\tCurrent directory is verified as ", os.getcwd())
    
# Open both input hiring files and read their contents
with open(chasHr, "r") as f:
    chasContents = f.readlines()
with open(auburHr, "r") as f:
    auburnContents = f.readlines()

# Checking if files are loaded properly
try:
    with open("WVDogsChasHR.txt", "r") as file1, open("WVDogsAuburnHR.txt", "r") as file2:
        # reading data from files
        data1 = file1.read()
        data2 = file2.read()
    print("\nHiring files successfully opened. BEGINNING PROCESSING.")
except FileNotFoundError:
    print("\nOne or both of the files could not be found.")
except IOError:
    print("\nThere was an error opening one or both of the files.")

# Combine them into a single data set and sort it ready for processing
combinedData = chasContents + auburnContents
sortedData = sorted([line.strip() for line in combinedData])

# Remove any lines containing semicolons
removedLines = [line for line in sortedData if ";" in line]
sortedData = [line for line in sortedData if ";" not in line]

print(" ")

# Prints to console SQL that is removed from the files
for line in removedLines:
    print("\tSQL Detected and Removed:", line)

print("\n\tHiring files vaildated and written to WVDogsCombinedHiring.txt ready for processing.")

file1.close()
file2.close()

print("\tAll files closed.")

# Write the validated, sorted hiring data to the combined file
with open(combinedHr, "w") as f:
    f.write("Employee Name\tJob Title\tSalary or Other Comp.\n")  # Add header row
    for line in sortedData:
        f.write(line + "\n")  # Write each line to the file

print(" ")
print('***** NEW EMPLOYEE INFORMATION *****'.center(60))

# Write the validated, sorted hiring data to the screen
print("{:<30}{:<30}{:<30}".format("\nEmployee Name", "Job Title", "Salary or Other Comp."))
print("{:-<30}{:-<30}{:-<30}".format("", "", ""))
for line in sortedData:
    fields = re.split(r"\t+", line)
    if len(fields) == 3:
        employeeName = fields[0].strip()
        jobTitle = fields[1].strip()
        payOrOtherComp = fields[2].strip()
        print("{:<30}{:<30}{:<30}".format(employeeName, jobTitle, payOrOtherComp))

print(" ")
print('***** HIRING REPORT COMPLETED *****'.center(60))

print()
print('--------------------------------'.center(60))
print('---    End Programming Assignment 3    ---'.center(60))
print('--------------------------------'.center(60))
