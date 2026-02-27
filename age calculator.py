from datetime import date
from time import sleep

print("Hello")
sleep(1)
years = int(input("enter your birth year: "))
months = int(input("enter your birth month: "))
days = int(input("enter your birth day: "))
birthday = date(years,months,days)
today = date.today()
year = int(date.today().year) - years
mon = year * 12
week = mon * 4
day = year * 365
hour = day * 24
print("how do you want to see your age: ")
calc = input("years =>'Y'    'months => M'    'weeks => W'    'days => D'    'hours => H'\n").lower().strip()
if calc == "y" or calc == "years":
    print("-"*40)
    print(f"you were born in {birthday}")
    print(f"you taking this test in {today}")
    print(f"your age in years is: {year}")
elif calc == "m" or calc == "months":
    print("-" * 40)
    print(f"you were born in {birthday}")
    print(f"you taking this test in {today}")
    print(f"your age in months is: {mon}")
elif calc == "w" or calc == "weeks":
    print("-" * 40)
    print(f"you were born in {birthday}")
    print(f"you taking this test in {today}")
    print(f"your age in weeks is: {week}")
elif calc == "d" or calc == "days":
    print("-" * 40)
    print(f"you were born in {birthday}")
    print(f"you taking this test in {today}")
    print(f"your age in days is: {day}")
elif calc == "h" or calc == "hours":
    print("-" * 40)
    print(f"you were born in {birthday}")
    print(f"you taking this test in {today}")
    print(f"your age in hours is: {hour:,}")
else:
    print("error")
print("happy birthday <3")
