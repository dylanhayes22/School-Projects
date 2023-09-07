#!/usr/bin/env python3
# Written by Dylan Hayes

from datetime import datetime, timedelta
import locale

def get_departure_date():
    date_str = input("Estimated date of departure (YYYY-MM-DD): ")
    departure_date = datetime.strptime(date_str, "%Y-%m-%d")
        
    return departure_date

def get_departure_time():
    time_str = input("Estimated time of departure (HH:MM AM/PM): ")
    departure_time = datetime.strptime(time_str, "%I:%M %p")
        
    return departure_time        

def main():
    print("Arrival Time Estimator")
    choice = "y"
    while choice.lower() == "y":            
        departure_date = get_departure_date()
        departure_time = get_departure_time()
        miles = input("Enter Miles: ")
        miles = float(miles)
        mph = input("Enter miles per hour: ")
        mph = float(mph)
        print()
                        
        print("Estimated travel time")
        travel_hours = miles / mph
        hours = int(travel_hours)
        minutes = round(travel_hours*60) % 60             
        print("Hours: ",hours)
        print("Minutes: ", minutes)
                        
        arrival_time = departure_time + timedelta(hours=hours) + timedelta(minutes=minutes)
        arrival_date = departure_date + timedelta(hours=hours) + timedelta(minutes=minutes)
        print("Estimated date of arrival: ", '{:%Y-%m-%d}'.format(arrival_date))
        print("Estimated time of arrival: ", '{:%I:%M %p}'.format(arrival_time))
                        
        print()
        choice = input ("Continue? (y/n): ")
        print()
    print("Bye!") 

if __name__ == "__main__":
        main()