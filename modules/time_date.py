import time

"""
It is Monday 22.April.2024 18:40:17 Uhr

%a abbreviated weekday name: Mon
%A full weekday name: Monday
%b abbreviated month name : Apr
%B full month name: April
%d Day of the month as a decimal number [01,31]: 22
%D Date format month/day/year : 04/22/24
%H Hour (24-hour clock) as a decimal number [00,23]: 18
%M Minute as a decimal number [00,59]: 40
%S Second as a decimal number [00,61]: 17
%y Year without century as a decimal number [00,99]: 24
%Y Year with century as a decimal number: 2024
%x Locale’s appropriate date representation: 04/22/24
%X Locale’s appropriate time representation: 18:43:06
"""


def get_time_date():
    """
    Returns a string with the actual date and the actual time.
    :return: now: str: e.g. 28.April.2024 07:45:07
    """
    now = time.strftime("%d.%B.%Y %H:%M:%S")
    return now


def get_time():
    """
    Returns a string with the actual time with hours, minutes and seconds separated by a colon.
    :return: now: str: e.g. 07:45:07
    """
    now = time.strftime("%H:%M:%S")
    return now


def get_date():
    """
    Returns a string with the actual date.
    :return: now: str: e.g. 28.April.2024
    """
    now = time.strftime("%d.%B.%Y")
    return now


if __name__ == "__main__":
    print(get_time_date())
    print(get_time())
    print(get_date())
