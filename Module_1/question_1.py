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