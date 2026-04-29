1. Create a program that calculates the estimated duration of a trip in hours and minutes (same time zone). This should include an estimated date/time of departure and an estimated date/time of arrival:

For the date of departure and arrival, the program should use the YYYY-MM-DD format for dates
For the time of departure and arrival , the program should use the HH:MM AM/PM format for times.
For the miles and miles per hour, the program should only accept integer entries like 200 and 65.
Assume that the user will enter valid data.


```python
from datetime import datetime, timedelta

print("Arrival Time Estimator")

# Setting up while loop
while True:
    date_of_departure = input("Estimated date of departure (YYYY-MM-DD): ")
    time_of_departure = input("Estimated time of departure (HH:MM AM/PM): ")
    miles = int(input("Enter miles: "))
    speed = int(input("Enter miles per hour: "))

    # Parsing with strptime
    departure_parsed = datetime.strptime(f"{date_of_departure} {time_of_departure}", "%Y-%m-%d %I:%M %p")

    # Math
    total_minutes = (miles / speed) * 60
    hours = int(total_minutes // 60)
    minutes = int(total_minutes % 60)


    # timedelta
    arrival_parsed = departure_parsed + timedelta(hours = hours, minutes = minutes)

    # Answer
    print("Estimated travel time")
    print(f"Hours: {hours}")
    print(f"Minutes: {minutes}")
    print(f"Estimated date of arrival: {arrival_parsed.strftime('%Y-%m-%d')}")
    print(f"Estimated time of arrival: {arrival_parsed.strftime('%I:%M %p')}\n")

    # Continue loop
    question = input("Continue? (y/n): ").lower()
    if question == "n":
        print("Bye!")
        break
```

    Arrival Time Estimator


    Estimated date of departure (YYYY-MM-DD):  2026-08-12
    Estimated time of departure (HH:MM AM/PM):  12:33 AM
    Enter miles:  456
    Enter miles per hour:  34


    Estimated travel time
    Hours: 13
    Minutes: 24
    Estimated date of arrival: 2026-08-12
    Estimated time of arrival: 01:57 PM
    


    Continue? (y/n):  N


    Bye!


2. Create a program that accepts a name and a birth date and displays the person’s birthday,the current day, the person’s age, and the number of days until the person’s next birthday.

Allow the user to enter a date in the MM/DD/YY format. Adjust the date so that it is correct even if the birth year is later than the current year.
When you calculate the person’s age, don’t take leap year into account. If the person is more than 2 years old, display the person’s age in years. Otherwise, display the person’s age in days.
When you display the message that indicates the number of days to the person’s birthday, you can use the following format for a person with a name of John: 
today - John's birthday is today!
tomorrow - John's birthday is tomorrow!
yesterday - John's birthday was yesterday!
other days - John's birthday is in X days


```python
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
```

    Birthday Calculator


3. Measure the time cost (efficiency) of an algorithm to use the computer’s clock to obtain an actual runtime. Via benchmarking/profiling implement an algorithm that counts from 1 to a million, time the algorithm and output the running time to the terminal window. Triple the problem size of this number and repeat this process. After four such increases, output the results of your program. For simplicity, measure the efficiency of the algorithm below.

#Start the algorithm
work = 1
for x in range(problemSize):
       work += 5
       work -= 5
#end of algorithm


```python
from datetime import datetime

problem_size = 1000000

print('Problem Size          Seconds')

for i in range(4):

    start = datetime.now()


    work = 1
    for x in range(problem_size):
        work += 5
        work -= 5

    end = datetime.now()
    time_delta = end - start
    seconds = time_delta.total_seconds()
    print(f"{problem_size:}               {seconds:}")
    problem_size = problem_size * 3
```

    Problem Size          Seconds
    1000000               0.128758
    3000000               0.268295
    9000000               0.80186
    27000000               2.425171



```python

```
