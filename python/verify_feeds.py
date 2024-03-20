from ics import Calendar
import requests
import argparse

# Inputs
parser = argparse.ArgumentParser()
parser.add_argument("--booking")
args = parser.parse_args()

c = Calendar(requests.get(args.booking).text)

print("Calendar")
print(c)
print("Events")
print(c.events)
e = list(c.timeline)[0]
print("Event '{}' started {}".format(e.name, e.begin.humanize()))
