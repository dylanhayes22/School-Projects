#!/usr/bin/env python3
# Written by Dylan Hayes

import locale as lc
from decimal import Decimal
from decimal import ROUND_HALF_UP

def title():
    print("Interest Calculator")
    print()
    
    
def total(loan, interest):
    rate = loan * (interest / 100)

def main():
    title()
    choice = "y"
    while choice.lower() == "y":
        loan = Decimal(input("Enter loan amount: "))
        interest = Decimal(input("Enter interest rate: "))
        interest = interest.quantize(Decimal("1.00"))
        rate = loan * (interest / 100)
        print()
        
        result = lc.setlocale(lc.LC_ALL, "")
        if result == "C":
            lc.setlocale(lc.LC_ALL, "en_US")        
        line = "{:20} {:>15}"
        
        print(line.format("Loan amount: ", lc.currency(loan, grouping=True)))
        print("Interest rate: {:>20.3f}%".format(interest))
        print(line.format("Interest amount: ", lc.currency(rate, grouping=True)))
        print()
        choice = input ("Continue? (y/n): ")
        print()
    print("Bye")


if __name__ == "__main__":
    main()