from datetime import datetime, timedelta

def get_birthdays_per_week(n):
    today = datetime.now().date()
    next_week = today + timedelta(days=(7 - today.weekday()) % 7)

    for i in range(7):
        current_day = next_week + timedelta(days=i)

        birthdays = {
            'Monday': [],
            'Tuesday': [],
            'Wednesday': [],
            'Thursday': [],
            'Friday': [],
            'Saturday': [],
            'Sunday': []
        }

        for user in n:
            name = user['name']
            birthday = user['birthday'].date()
            day_of_week = birthday.strftime('%A')

            if day_of_week in ['Saturday', 'Sunday']:
                day_of_week = 'Monday'

            if current_day.strftime('%A') == day_of_week and today <= birthday <= current_day:
                birthdays[day_of_week].append(name)

        if birthdays[current_day.strftime('%A')]:
            print(f"{current_day.strftime('%A')}: {', '.join(birthdays[current_day.strftime('%A')])}")


users = [
    {'name': 'Nastya', 'birthday': datetime(2023, 7, 27)},
    {'name': 'Yura', 'birthday': datetime(2023, 7, 26)},
    {'name': 'Sofia', 'birthday': datetime(2023, 7, 25)},
    {'name': 'Ernest', 'birthday': datetime(2023, 7, 20)},
]

if __name__ == '__main__':
    get_birthdays_per_week(users)




