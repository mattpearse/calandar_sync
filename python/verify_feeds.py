from ics import Calendar
import requests
import argparse

# Inputs
parser = argparse.ArgumentParser()
parser.add_argument("--booking")
args = parser.parse_args()

c = Calendar(requests.get(args.booking).text)

c
c.events
e = list(c.timeline)[0]
"Event '{}' started {}".format(e.name, e.begin.humanize())
