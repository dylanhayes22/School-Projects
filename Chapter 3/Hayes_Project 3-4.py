#!/usr/bin/env python3
# written by Dylan Hayes

# display a welcome message

print("===============================================================")
print("Shipping Calculator")
print("===============================================================")


choice = "y"
while choice.lower() == "y":

    # order cost
    order_cost = float(input("Cost of items ordered:\t "))

    # shipping cost
    if order_cost >= 0 and order_cost < 30.00:
        print("Shipping Cost:\t\t", 5.95)
        print("Total Cost:\t\t", round(order_cost + 5.95, 2))
    
    elif order_cost >= 30.00 and order_cost <= 49.99:
        print("Shipping Cost:\t\t", 7.95)
        print("Total Cost:\t\t", round(order_cost + 7.95, 2))

    elif order_cost >= 50.00 and order_cost <= 74.99:
        print("Shipping Cost:\t\t", 9.95)
        print("Total Cost:\t\t", round(order_cost + 9.95, 2))

    elif order_cost >= 75.00:
        print("Shipping Cost:\t\t", "FREE")
        print("Total Cost:\t\t", order_cost)
        
    else:
        print("You must enter a positive number. Please try again.")
        continue
        
    print()    
    choice = input("Continue (y/n)? ")
    print("===============================================================")

print("Bye!")


