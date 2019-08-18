# Python program to print today's date and time

import datetime


def get_date(current_time):
    return "{0}/{1}/{2}".format(current_time.day, current_time.month, current_time.year)


def get_time(current_time):
    return "{0}:{1} {2}".format(current_time.hour, current_time.minute, current_time.second)


print('Date - ', get_date(datetime.datetime.now()))
print('Time - ', get_time(datetime.datetime.now()))
