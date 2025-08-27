import calendar
import datetime

def get_tuesdays_and_fridays(year: int, month: int):

    days = []
    total_days = calendar.monthrange(year, month)[1]

    for day in range(1, total_days + 1):
        date = datetime.date(year, month, day)
        if date.weekday() in [1, 4]:  # Tue=1, Fri=4
            days.append(date.strftime("%Y-%m-%d"))
    return days

# Example
if __name__ == "__main__":
    print(get_tuesdays_and_fridays(2025, 9))
