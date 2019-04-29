'''
Learning and using the datetime module
'''

import datetime
import time

f = time.clock()

# working with dates, creates a date 
d = datetime.date(2018, 11, 7)
print (d)

# for today date 
tday = datetime.date.today()
print (tday)
print (tday.isoweekday())

# time deltas diff btw dates and times
tdelta = datetime.timedelta(days=7)

# time a week from now
print (tday+tdelta)

# diff in dates results timedelta
bday = datetime.date(2019, 7, 1)

till_bday = bday - tday
print (till_bday) # or till_bday.days for days, .total_seconds() for seconds

# working with hours mins secs n micro secs
t = datetime.time(9, 30, 45, 100000)
print (t,)  # t.hour

# working with both
dt = datetime.datetime(2018, 12, 7, 6, 48, 30, 0)
print (dt)
print (dt.date())
print (dt.time())

# time since the first call to clock
f2 = time.clock()
print ("time to run " + str(f2-f))
print (time.ctime())    # prints current time and date