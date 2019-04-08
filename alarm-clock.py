# Python Alarm Clock
# Starting program and select month, date, time and song to wake up to
import sys
import datetime
import re
import time

print("""
    Enter the time for the alarm.  Month only needs to be specified if its not this month.  Valid inputs are
    '9:00 PM' - Today at 9PM
    'Tommorow 7:00 AM' - Tomorrow at 7 AM
    '25 AUG 6:00 AM' - The date in the future
    'Friday 5:00' - The next Friday at 5 AM
""")
alarm = input('Enter a month: ')
days_of_week = ("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
other_days = ("Tomorrow")
months = ("January", "February", "March")

current_time = datetime.datetime.now()
month = current_time.month
year = current_time.year
day = current_time.day

time_re = re.compile(r'\d+:\d+')
alarm_hour = int(time_re.search(alarm).group().split(':')[0])
if 'PM'.lower() in alarm.lower():
    alarm_hour += 12
alarm_minute = int(time_re.search(alarm).group().split(':')[1])

alarm_time = datetime.datetime(year, month, day, int(alarm_hour), alarm_minute)
wait_time = alarm_time.timestamp() - current_time.timestamp()
print(f'Alarm will go off at {alarm_time}')
print(f'seconds until the alarm are {wait_time}')
time.sleep(wait_time)
print("It's alarm time now!!!!")
