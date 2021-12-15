#!/usr/bin/env python3
# written by Dylan Hayes

# display a welcome message
print("Tip Calculator")
print()


# cost of meal
meal_cost = float(input("Cost of Meal:\t"))
print()

# tip amount
print("15%")
print("Tip amount: ", round(meal_cost*.15, 2))
print("Total amount:", round(meal_cost + meal_cost*.15, 2))
print()

print("20%")
print("Tip amount: ", round(meal_cost*.20, 2))
print("Total amount:", round(meal_cost + meal_cost*.20, 2))
print()

print("25%")
print("Tip amount: ", round(meal_cost*.25, 2))
print("Total amount:", round(meal_cost + meal_cost*.25, 2))