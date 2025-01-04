from ics import Calendar
from datetime import datetime
import sys
import requests
import argparse
import modules

# Inputs
parser = argparse.ArgumentParser()
parser.add_argument("args", nargs="*")
parser.add_argument("--end")
args = parser.parse_args()
end_date = datetime.strptime(args.end, "%Y-%m-%d").date()
today = datetime.now()
cal_count = 0
cals = []
dates = []
prev = ""
count = 1
errors = 0

for url in args.args:
    cals.append( Calendar(requests.get(url).text) )
    cal_count += 1

#print("Calendar")
#print(c)
#print("Events")
#print(c.events)

for cal in cals:
    for e in cal.timeline:
        eb = e.begin.format("YYYY-MM-DD")
        ee = e.end.format("YYYY-MM-DD")
        print("Booking from ", eb, " to ", ee)
        first = 1
            
        for date in modules.get_list_of_dates(eb, ee):
            if eb == prev and first == 1:
                first = 0
                continue
            dates.append(date)
        prev = ee

dates.sort()
prev = ""

for date in dates:
    print("Debug - ", date)
    if date <= today:
        print("Skipping..")
        continue
    if prev == "":
        prev = date
    elif date != prev:
        if count != cal_count:
            print("Problem date", prev)
            errors += 1
        if date > end_date:
            print("No checking beyond", end_date)
            break
        prev = date
        count = 1
    else:
        count += 1

if errors > 0:
    print("There were", errors, "errors")
    sys.exit(1)
else:
    print("No errors")
