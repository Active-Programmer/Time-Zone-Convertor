import pytz
import datetime

year = int(input("Year = "))
month = int(input("month = "))
day = int(input("day = "))
hour = int(input("hour = "))
minute = int(input("minute = "))

user_time = datetime.datetime(year, month, day, hour, minute)

# converting to timezone

delhi_timezone = pytz.timezone("Asia/Kolkata")
london_timezone = pytz.timezone("UTC")

utc_time = pytz.utc.localize(user_time)

delhi_time = utc_time.astimezone(delhi_timezone)
london_time = utc_time.astimezone(london_timezone)

print("Delhi Time is :", delhi_time.isoformat())
print("London Time is :", london_time.isoformat())
