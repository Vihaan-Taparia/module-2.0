#Current date and time
from datetime import date,time,datetime
#Calling the today
#functon of date class
today = date.today()
now = datetime.now()
print("Todays date is",today)
print("The time right now is",now)

#Printing dates components
print("\nData components",today.year,today.month,today.day)


