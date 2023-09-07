# Dylan Hayes
# AIST 2120, PA 1 – Ch. 3 
#! Python 3
# 1/30/2023

print()
print('--------------------------------'.center(60))
print('---        AIST 2120         ---'.center(60))
print('---   Pgm. Assgn. 1: SERIES      ---'.center(60))
print('---    By Dylan Hayes   ---'.center(60))
print('--------------------------------'.center(60))
print()

# Gets userinput and validates that is a integar
while True:
    try:
        seconds = int(input("How many seconds (integar) has the computer virus been replicating? "))
        if seconds >= 0:
            break
        else:
            print("Input must be a non-negative integar")
    except ValueError:
        print("Input must be a non-negative integer.")

# Takes userinput and calulates the memory the virus as taken.
def calculate_size(seconds):
    x = 1
    mem = 1024
    
    print(" ")
    print("Calculating virus memory utilization after " + str(seconds) + " seconds.")
    
    while x <= seconds:
        if seconds == 0:
            print("\tCalculating virus memory utilization after 0 seconds.")
            break
        else:
            mem = mem * 2
            print("\tAt t+" + str(x) + ", memory calculation double to " + str(mem))
            x += 1
    print(" ")
    print("\tVirual memory utilization calculation complete!")
    return mem

# calls function
result = calculate_size(seconds)

print(" ")
print("The virus is using {} bytes of memory".format(result))

print()
print('--------------------------------'.center(60))
print('---    End Programming Assignment 1    ---'.center(60))
print('--------------------------------'.center(60))
