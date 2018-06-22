import datetime

#print a specific date --- datetime.date(year, month, day)
custom_date = datetime.date(2016, 7, 24)
print(custom_date)

#print the current data --- datetime.date.today()
tday = datetime.date.today()
print('**'*10)
print(f'Current date {tday}\nYear {tday.year}\nDay {tday.day}\nMonth {tday.month}')
print('**'*10)

#to get time in the future or the past -- datetime.delta(days = 7 or hours = 7)
tdelta = datetime.timedelta(days = 7)
print(f'Original Date {tday}\nDelta date {tday + tdelta}')

#timedelta = date1 - date2 
#timedelta = date1 + date2
bday = datetime.date(2018, 7, 26)
current_date = datetime.date.today()
till_birthday = bday - current_date
print(f'\n{till_birthday.days} days left to your birthday')

#to get a specific time -- datetime.time() 
randDate = datetime.time(12, 5, 54, 10000)
print(f'\n{randDate} random date with datetime.time() method (NOT RECOMMENDED)')

#to get date with time together -- datetime.datetime(y, m, d, hours, min, sec, msec) 
dt = datetime.datetime(2016, 5, 20, 8, 20, 30, 10000)
print(f'\n{dt}\n{dt.time()}\nYear: {dt.year}\nHour: {dt.hour}')
print("This method is recommended")

timedelta = datetime.timedelta(hours = 7)
print(f'\nOriginal date: {dt}\nDelta date: {dt + timedelta} (Time Changed)')
