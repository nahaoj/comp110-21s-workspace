"""A vaccination calculator."""

__author__ = "930410205"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...

print("Enter population size: ")
population = int(input())

print("Enter doses administered: ")
admin = int(input())

print("Enter doses per day: ")
daily_doses = int(input())

print("Enter target percent vaccinated: ")
target_percentage = int(input())

days_needed = int((2*(population - admin)*target_percentage)/(100 * daily_doses))

import math
days_needed = math.ceil(days_needed)

from datetime import datetime, timedelta
today: datetime = datetime.today()
days_until: timedelta = timedelta(days_needed)
vaccination_date: datetime = today + days_until
vaccination_date = vaccination_date.strftime("%B %d, %Y")
vaccination_date = str(vaccination_date)

print("Population: " + str(population))
print("Doses administered: " + str(admin))
print("Doses per day: " + str(daily_doses))
print("Target percent vaccinated: " + str(target_percentage))
print("We will reach " + str(target_percentage) + "% vaccination in " + str(days_needed) + " days, which falls on " + str(vaccination_date) + ".")
