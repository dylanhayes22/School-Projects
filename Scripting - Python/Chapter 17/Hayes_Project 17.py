#!/usr/bin/env python3
# Written by Dylan Hayes

from pathlib import Path    # object oriented
import os
import shutil
import socket    

path = "/Temp/hayesIP_Project_Folder"

def ipv4():
    # Get Ipv4 address and check what class it is
    address = socket.gethostbyname(socket.gethostname())
    address_split = address.split(".")
    first = address_split[0]
    first = int(first)

    if first >= 0 and first < 128:
        first = "A"
        
    elif first >= 128 and firs < 192:
        first = "B"
        
    elif first >= 192 and first < 224:
        first = "C"
        
    elif first >= 224 and first < 240:
        first = "D"
        
    elif xxxxs[0] >= 240:
        first = "E"
    
    # Get octects, convert to int and join to get binary and hexadecimal
    first_octect = address_split[0]
    first_octect = int(first_octect)
    second_octect = address_split[1]
    second_octect = int(second_octect)
    third_octect = address_split[2]
    third_octect = int(third_octect)
    forth_octext = address_split[3]
    forth_octext = int(forth_octext)
    
    join = first_octect + second_octect + third_octect + forth_octext
    
    bin1 = bin(first_octect)
    bin2 = bin(second_octect)
    bin3 = bin(third_octect)
    bin4 = bin(forth_octext)
    
    bin_list = (bin1,bin2,bin3,bin4)
    full_bin = ".".join(bin_list)
    
    hex1 = hex(first_octect)
    hex2 = hex(second_octect)
    hex3 = hex(third_octect)
    hex4 = hex(forth_octext)
    
    hex_list = (hex1,hex2,hex3,hex4)
    full_hex = ".".join(hex_list)
    
    #Printing the results
    print("This IPv4 address is: ", address)
    print("This address is a class: ", first)
    print("Your IPv4 address in binary is as follows: ", full_bin )    
    print("Your IPv4 address in hex is as follows: ", full_hex)
    
    create(address, first, full_bin, full_hex)
    
    return(address, first, full_bin, full_hex)

    
def create(address, first, full_bin, full_hex):
    
    try:
        os.makedirs(path)
    except OSError:
        print("Directory %s is already created" % path)
    else:
        print("Successfully created the directory %s " % path)
        

    ipv4_list = [address, first, full_bin, full_hex]
    
    os.chdir("/temp/hayesIP_Project_Folder")
    
    f = open("hayesIP_Project_File.txt", "w")
    for line in ipv4_list:
        f.write(line)
        f.write("\n")
    f.close()


def main():
    ipv4()

    
if __name__ == "__main__":
    main()

