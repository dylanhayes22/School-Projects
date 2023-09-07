# Dylan Hayes
# AIST 2120: Programming Assignment 6
# 04/26/2023

print()
print('--------------------------------'.center(60))
print('---        AIST 2120         ---'.center(60))
print('---   Pgm. Assgn. 6: Encryptinator Plus      ---'.center(60))
print('---    By Dylan Hayes   ---'.center(60))
print('--------------------------------'.center(60))
print()

import os
import time
import json
import PyPDF2
import sys

# Set current working directory and print it to screen
cwd = os.getcwd()
if not os.path.basename(cwd) == "Pgm Asgn 6 Folder":
    os.chdir("Pgm Asgn 6 Folder")
    cwd = os.getcwd()
print(f"Current Working Directory: {cwd}\n")

# Look through the Source folder
src_folder = os.path.join(cwd, 'Source')
pdf_files = [f for f in os.listdir(src_folder) if os.path.isfile(os.path.join(src_folder, f)) and f.endswith('.pdf')]

# Print all files in Source folder
print("Procssing folder: ./Source/")
print("\n\tFiles in ./Source/ folder:")
for f in os.listdir(src_folder):
    if os.path.isfile(os.path.join(src_folder, f)):
        print("\t\t" + f)

print("\n\t\t***********************")

#Encrypt PDF files and write to Destination folder
print("\nProcessed folder: ./Destination/")
print("\n\tProcessed files in ./Destination/ folder:")
processing_times = {}
dest_folder = os.path.join(cwd, 'Destination')
for pdf_file in pdf_files:

    # Open PDF file
    start_time = time.perf_counter()
    with open(os.path.join(src_folder, pdf_file), 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)
        pdf_writer = PyPDF2.PdfWriter()
        
        # Apply encryption to PDF file using password "enigma"
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])
        pdf_writer.encrypt("enigma")
        
        # Write encrypted PDF file to Destination folder with prefix "encrypted_"
        new_pdf_name = f"encrypted_{pdf_file}"
        with open(os.path.join(dest_folder, new_pdf_name), 'wb') as output:
            pdf_writer.write(output)

    # Record processing time and add to dictionary
    end_time = time.perf_counter()
    processing_time = round(end_time - start_time, 2)
    processing_times[pdf_file] = processing_time

# Print original filenames of PDFs in Destination folder
for pdf_file in sorted(os.listdir(dest_folder)):
    if pdf_file.endswith('.pdf'):
        print("\t\t- " + (pdf_file))
    
# Write processing times to JSON file
json_file = os.path.join(cwd, 'time_file.json')
with open(json_file, 'w') as f:
    json.dump(processing_times, f, indent=4)

# Print time data for each PDF from time_file.json
print("\nTime data for each PDF is as follows:")
with open(json_file, 'r') as f:
    data = json.load(f)
    for k, v in data.items():
        print(f"\t\t{k}: {v}")
        
print("\nThe JSON time_file created.")

print("\n*** File processing completed! ***")

enigma_description = """
Enigma was an encryption machine used by the Germans during World War II for 
ciphering and deciphering secret messages. It was considered highly secure at 
the time, and its encrypted communications were a challenge for the Allies. 
However, a team of mathematicians and cryptanalysts led by the British 
mathematician Alan Turing managed to crack the Enigma code. The decryption of 
Enigma-encoded messages significantly contributed to the Allied victory, as it 
allowed them to anticipate and counter German military strategies. The work on 
breaking the Enigma code also played a crucial role in the development of 
computers and computer science."""

print("\nBONUS:" + enigma_description)

sys.exit

print()
print('--------------------------------'.center(60))
print('---    End Programming Assignment 6    ---'.center(60))
print('--------------------------------'.center(60))