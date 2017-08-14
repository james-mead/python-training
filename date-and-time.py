"""Example of date and time."""

import time

timeNow = time.localtime(time.time())
timeAsc = time.asctime()

print(timeNow)
print(timeNow[0:3])  # get year, month and date
print(timeAsc)
