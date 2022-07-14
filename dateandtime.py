#Date and Time
import datetime as dt

current_date=dt.date.today()
print("current date:",current_date)
new=dt.date(2021,12,7)
print(new)
print("year:",new.year)
print("month:",new.month)
print("day:",new.day)
print('-----------Time-------------')
a=dt.time(10,45,54,50849)
print(a)
print("Hour:",a.hour)
current_time=dt.datetime.now()
print("Current time:",current_time)
new=dt.datetime(2022,5,20,12,25,20,54324)
print(new,'Create time')
print(new.date())
print(new.time())
print('-----------Difference----------')
current=dt.datetime.now()
new_year=dt.datetime(2023,1,1)
difference=new_year-current
print(difference)
print('-------------------------------')
current=dt.datetime.now()
print(current)
s=current.strftime("%A %b %d %Y")
print(s)

#output
current date: 2022-07-11
2021-12-07
year: 2021
month: 12
day: 7
-----------Time-------------
10:45:54.050849
Hour: 10
Current time: 2022-07-11 16:00:29.224371
2022-05-20 12:25:20.054324 Create time
2022-05-20
12:25:20.054324
-----------Difference----------
173 days, 7:59:30.774623
-------------------------------
2022-07-11 16:00:29.225704
Monday Jul 11 2022