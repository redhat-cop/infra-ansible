import datetime
import dateutil.parser
from dateutil.rrule import rrule


# Parse valid date string to an Ansible-friendly datetime object
def parse_datetime(ds, **kwargs):
    return dateutil.parser.parse(ds)

# Add time to datetime objects
def add_time(dt, **kwargs):
    return dt + datetime.timedelta(**kwargs)

# Subtract time from datetime objects
def subtract_time(dt, **kwargs):
    return dt - datetime.timedelta(**kwargs)

# Creates an rrule from a datetime object and dateutil.rrule, for example freq and count
def to_rrule(dtstart, **kwargs):
    return str(rrule(dtstart=dtstart, **kwargs)).replace('\n', ';')

class FilterModule(object):
    def filters(self):
        return {
            'parse_datetime': parse_datetime,
            'add_time': add_time,
            'subtract_time': subtract_time,
            'to_rrule': to_rrule,
        }
