import time
import datetime

seconds = "{:,.4f}".format(time.time())
scientific = "{:.2e}".format(time.time())
print("Seconds since January 1, 1970: ", seconds, "or", scientific, "in scientific notation")

date = datetime.datetime.now()
print(date.strftime("%b"), date.day, date.year)