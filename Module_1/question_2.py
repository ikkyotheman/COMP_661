from datetime import datetime, timedelta
print("Birthday Calculator")
# while loop
while True:
    name = input("Enter name: ")
    bday = input("Enter birthday (MM/DD/YY): ")
    # strptime on bday
    bday_parsed = datetime.strptime(bday, "%m/%d/%y")
    today = datetime.today()
    if bday_parsed.year > today.year:
        bday_parsed = datetime(bday_parsed.year - 100, bday_parsed.month, bday_parsed.day)
    # strftime
    print(f"Birthday:  {bday_parsed.strftime('%A, %B %d, %Y')}")
    print(f"Today:     {today.strftime('%A, %B %d, %Y')}")
    # math
    age_in_days = (today - bday_parsed).days
    age_in_years = age_in_days // 365
    # years or days
    if age_in_years> 2:
        print(f"{name} is {age_in_years} years old.")
    else:
        print(f"{name} is {age_in_days} days old.")
    next_bday = datetime(today.year, bday_parsed.month, bday_parsed.day)
    # change date if bday passed
    if next_bday < today:
        next_bday = datetime(today.year + 1, bday_parsed.month, bday_parsed.day)
    days_until = (next_bday - today).days
    # bday message
    if days_until == 0:
        print(f"{name}'s birthday is today!")
    elif days_until == 1:
        print(f"{name}'s birthday is tomorrow!")
    elif days_until == 364 or days_until == 365:
        print(f"{name}'s birthday was yesterday!")
    else:
        print(f"{name}'s birthday is in {days_until} days.")
    question = input("Continue? (y/n): ").lower()
    if question == "n":
        print("Bye!")
        break