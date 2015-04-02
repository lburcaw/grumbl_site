#!/usr/bin/python

from datetime import datetime, date
import calendar

def dayofyear(datestr):
    date = datetime.strptime(datestr, '%B %d')
    day = int(date.strftime('%j'))
    return day

def monthofyear(datestr):
    date = datetime.strptime(datestr, '%B %d')
    month = int(date.strftime('%m'))
    return month

def lastdayofmonth(month):
    last_daymonth = calendar.monthrange(2014,month)
    return last_daymonth[1]
    
def monthdaysofyear(month,last_daymonth):
    first_day = date(year=2014,month=month,day=1)
    last_day = date(year=2014,month=month,day=last_daymonth)
    first_doy = int(first_day.strftime('%j'))
    last_doy = int(last_day.strftime('%j'))
    doy_range = range(first_doy,last_doy+1)
    return doy_range