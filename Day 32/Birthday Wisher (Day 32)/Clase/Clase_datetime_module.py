import datetime as dt
#Chaning the name of the importation to now confuse the library with the class
#Using the method now() to get the real time date,hour.

now = dt.datetime.now()
#The now object has the information as attributes, so to can tap into then by calling them with the dot notation
year = now.year
month = now.month
day = now.day
#if we want to know the day of the week, we can use the weekday method.
day_of_week = now.weekday()
hour = now.hour
seconds = now.second
print(day, day_of_week,month)
#We can create an object with the specific attributes that we want to hold. Ejemplo : my date of birth
my_date_of_bith = dt.datetime(month=6, day=28, year=1994)
print(my_date_of_bith)
