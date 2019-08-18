# Python program to print today's date and time

import datetime


def get_date():
    return str(datetime.date.today())


def get_time():
    return str(datetime.time.hour)


print('Date - ', get_date())
print('Time - ', get_time())
