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
alarm = input('Enter the time for the alarm: ').lower()
days_of_week = ("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
other_days = ("tomorrow")
months = ("january", "february", "march", "april", "may", "june", "july", "august", "september", "october","november", "december")

current_time = datetime.datetime.now()

# Find the month
alarm_month = current_time.month
for month in months:
    if month in alarm:
        alarm_month = months[month]

# Find the Year
year_re = re.complie(r'\d\d\d\d'):
if year_re.search(alarm):
    alarm_month = year_re.search(alarm).group()
else:
    alarm_year = current_time.year


currentyday = current_time.day

time_re = re.compile(r'\d+:\d+')
alarm_hour = int(time_re.search(alarm).group().split(':')[0])
if 'PM'.lower() in alarm.lower():
    alarm_hour += 12
alarm_minute = int(time_re.search(alarm).group().split(':')[1])

alarm_time = datetime.datetime(year, alarm_month, day, int(alarm_hour), alarm_minute)
wait_time = alarm_time.timestamp() - current_time.timestamp()
print(f'Alarm will go off at {alarm_time}')
print(f'seconds until the alarm are {wait_time}')
time.sleep(wait_time)
print("It's alarm time now!!!!")
