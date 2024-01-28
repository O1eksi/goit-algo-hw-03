from datetime import datetime, timedelta

def get_upcoming_birthdays(users):

    #Determine the current date
    today = datetime.today().date()

    upcoming_birthdays = []

    #Convert birthdates from strings to datetime objects
    for user in users:
        #user["birthday"] = datetime.strptime(user["birthday"], "%Y.%m.%d").date() 
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday_date.replace(year=today.year)
        
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_until_birthday = (birthday_this_year - today).days

        if 0 <= days_until_birthday <= 7:
            if birthday_this_year.weekday() in [5, 6]:  # If birthday falls on a weekend
                days_until_birthday += (7 - birthday_this_year.weekday())

            congratulation_date = today + timedelta(days=days_until_birthday)
            congratulation_date_str = congratulation_date.strftime("%Y.%m.%d")

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date_str
            })

    return upcoming_birthdays







users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.29"},
    {"name": "John Doe", "birthday": "1985.05.23"},
    {"name": "Jane Smith", "birthday": "1990.09.27"},
    {"name": "John Doe", "birthday": "1985.01.31"},
    {"name": "Jane Smith", "birthday": "1990.12.27"}
]


print(get_upcoming_birthdays(users))

