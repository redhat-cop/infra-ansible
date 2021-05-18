from ansible.errors import AnsibleError
from datetime import datetime, timedelta
from dateutil.parser import parse
from dateutil.rrule import rrule, DAILY
import pytz


def parse_datetime(datestring):

    # Parses ISO date string and converts to datetime object.
    return parse(datestring)


def set_time(dt, hour, minute):

    # Set the time to a specific hour, minute
    return dt.replace(hour=hour, minute=minute)


def set_timezone(dt, tz):

    # Unset existing timezone
    dt = dt.replace(tzinfo=None)
    # Set the timezone
    tz = pytz.timezone(tz)

    # Normalize the timezone offset based on the datetime
    return tz.normalize(tz.localize(dt))


def add_time(dt, **kwargs):

    # Calculate future datetime object.
    return dt + timedelta(**kwargs)


def subtract_time(dt, **kwargs):

    # Calculate past datetime object.
    return dt - timedelta(**kwargs)


def to_rrule(dt, **kwargs):

    """
    Converts datetime object to recurrence rule in the format accepted by the
    Ansible Tower /api/v2/{resource}/{id}/schedules/ endpoint
    """

    options = {
        "freq": DAILY,
        "interval": 1,
        "count": 1,
        "timezone": "Zulu",
    }
    options.update(kwargs)
    # Pop timezone from options for later use
    timezone = options.pop("timezone")
    my_rrule = rrule(dtstart=dt, **options)
    # Validate timezone name and add to RRULE using some string manipulation
    if timezone not in pytz.all_timezones:
        raise AnsibleError("Timezone is not valid")
    return_rrulestr = (
        str(my_rrule)
        .replace("\n", " ")
        .replace("DTSTART:", "DTSTART;TZID={0}:".format(timezone))
    )
    # Add interval again as required by Tower API if omitted by rrule module
    if "INTERVAL" not in return_rrulestr:
        return_rrulestr = "{0};INTERVAL=1".format(return_rrulestr)
    return return_rrulestr


class FilterModule(object):

    """
    A set of filters to convert a standard ISO date string to a datetime object,
    then add or subtract time before converting to an Ansible Tower/AWX compatible
    recurrence rule (rrule).
    """

    def filters(self):
        return {
            "parse_datetime": parse_datetime,
            "set_time": set_time,
            "set_timezone": set_timezone,
            "add_time": add_time,
            "subtract_time": subtract_time,
            "to_rrule": to_rrule,
        }
