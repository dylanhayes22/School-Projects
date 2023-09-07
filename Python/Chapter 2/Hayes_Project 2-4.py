#!/usr/bin/env python3
# Written by Dylan Hayes

# display a welcome message
print("Price Comparison")
print()

# get prcies from the user
price_64 = float(input("Price of 64 oz size: "))
price_32 = float(input("Price of 32 oz size: "))

# calcute price per ounce
peroz_64 = round(price_64 / 64, 2)
peroz_32 = round(price_32 / 32, 2)

#format and display the result
print()
print("Price per oz (64 oz): " + str(peroz_64))
print("Price per oz (32 oz): " + str(peroz_32))