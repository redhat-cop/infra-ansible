from datetime import timedelta
from dateutil.parser import parse
from dateutil.rrule import rrule


def parse_datetime(datestring):

    # Parses ISO date string and converts to datetime object.
    return parse(datestring)


def add_time(dt, **kwargs):

    # Calculate future datetime object.
    return dt + timedelta(**kwargs)


def subtract_time(dt, **kwargs):

    # Calculate past datetime object.
    return dt - timedelta(**kwargs)


def to_rrule(dt, **kwargs):

    """
    Converts datetime object to recurrence rule in the format required by the
    Ansible Tower/AWX /api/v2/project/{id}/schedules/ endpoint:
    DTSTART:YYYYMMDDTHHMMSSZ RRULE:FREQ=MINUTELY,INTERVAL=10,COUNT=5

    Note that interval is required by the Tower/AWX api but omitted
    by the rrule module if = 1
    """
    r_rule = str(rrule(dtstart=dt, **kwargs)).split("\n")
    if "RRULE" not in r_rule[1]:
        parts = ["Z RRULE:" + r_rule[1]]
    else:
        parts = ["Z " + r_rule[1]]
    if "INTERVAL" not in r_rule[1]:
        parts.append("INTERVAL=1")
    return r_rule[0] + ";".join(parts)


class FilterModule(object):

    """
    A set of filters to convert a standard ISO date string to a datetime object,
    then add or subtract time before converting to an Ansible Tower/AWX compatible
    recurrence rule (rrule).
    """

    def filters(self):
        return {
            "parse_datetime": parse_datetime,
            "add_time": add_time,
            "subtract_time": subtract_time,
            "to_rrule": to_rrule,
        }
