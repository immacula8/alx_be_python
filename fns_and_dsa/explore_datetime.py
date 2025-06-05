from datetime import datetime, timedelta

def display_current_datetime ():

    current_date = datetime.now()

    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

    print("current Date and Time:", formatted_date)


def calculate_future_date():

    try:
        user = int(input("Enter number of days:"))
        days = int(user)
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days)

        formatted_date = future_date.strftime("%Y-%m-%d")
        print(f"\nThe date {days} day(s) from now will be: {formatted_date}")
    except ValueError:
        print("Please enter  valid number.")

display_current_datetime()
calculate_future_date()