from datetime import datetime, timedelta

# Create list of dates when passed start and end
def get_list_of_dates(start, end):
    dates = []
    s = datetime.strptime(start, "%Y-%m-%d").date()
    e = datetime.strptime(end, "%Y-%m-%d").date()
    for x in range(0, (e - s).days + 1):
        dates.append( (s + timedelta(days=x)) )
    return dates
