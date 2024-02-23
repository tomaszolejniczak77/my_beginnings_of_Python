from datetime import date, datetime

today = datetime.now()
enddate = date(today.year, today.month, today.day)


def get_difference(startdate):
    diff = enddate - startdate
    return diff.days
