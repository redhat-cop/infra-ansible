from ansible.errors import AnsibleError
from datetime import datetime, timedelta
from dateutil.parser import parse
from dateutil.rrule import rrule, DAILY
import pytz


def parse_datetime(datestring, **kwargs):

    # Parses ISO date string and converts to datetime object.
    return parse(datestring)


def replace_datetime(dt, **kwargs):

    """
    Return a datetime with the same attributes, except for those attributes given new values by whichever keyword arguments are specified.
    Docs: https://docs.python.org/3/library/datetime.html#datetime.datetime.replace
    Example to convert a datestring to datetime object and set to America/New_York timezone at exactly midnight:
    midnight_eastern: |-
      {{ '2006-01-02T15:04:05.999-0700'
      | parse_datetime
      | replace_datetime(hour=0, minute=0, second=0, microsecond=0, tzinfo='America/New_York') }}
    Output:
      midnight_eastern: '2006-01-02 00:00:00-05:00'
    """

    new_dt = dt
    if "tzinfo" in kwargs:
        if kwargs["tzinfo"] not in pytz.all_timezones:
            raise AnsibleError("Timezone is not valid: {0}".format(kwargs["tzinfo"]))
        tzinfo = pytz.timezone(kwargs.pop("tzinfo"))
        dt = dt.replace(tzinfo=None)
        new_dt = tzinfo.normalize(tzinfo.localize(dt))
    return new_dt.replace(**kwargs)


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
    # Add and override default options as needed
    options.update(kwargs)

    # Timezone needs to be processed separately from rrule
    timezone = options.pop("timezone")
    my_rrule = rrule(dtstart=dt, **options)
    if timezone not in pytz.all_timezones:
        raise AnsibleError("Timezone is not valid: {0}".format(timezone))

    # Add TZID now that we have a valid rrule
    return_rrulestr = (
        str(my_rrule)
        .replace("\n", " ")
        .replace("DTSTART:", "DTSTART;TZID={0}:".format(timezone))
    )
    # Note that interval is required by the Tower/AWX api but omitted by the rrule module if interval=1
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
            "replace_datetime": replace_datetime,
            "add_time": add_time,
            "subtract_time": subtract_time,
            "to_rrule": to_rrule,
        }
