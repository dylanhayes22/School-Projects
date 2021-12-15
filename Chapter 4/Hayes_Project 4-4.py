#!/usr/bin/env python3
# written by Dylan Hayes

# taxes
def taxes(item_cost, total):
    global sale_tax
    
    sale_tax = float(round(total*.06, 2))
    total_tax = total + sale_tax
    
    return total_tax

# welcome message
print("Sales Tax Calculator")
print()
print("ENTER ITEMS (ENTER 0 TO END)")

def main():
    global sale_tax

    # user input
    total = 0
    for i in range(1):
        choice = "y"
        while choice.lower() == "y":
            item_cost = float(input("Cost of item: "))       
            if item_cost > 0:
                total += item_cost
                sale_tax = taxes(item_cost, total)
                total_tax = taxes(item_cost, total)            
                continue
            elif item_cost == 0:
                print("Total:\t\t ", total)
                print("Sales tax:\t ", round(sale_tax, 2))
                print("Total after tax: ", round(total_tax, 2))
                
            
            print()
            choice = input("Again? (y/n): ")
            total = 0
            print()

        print()
        print("Thanks, Bye!")

if __name__ == "__main__":
    main()