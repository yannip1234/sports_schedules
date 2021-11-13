from django import template
import datetime
import pytz

register = template.Library()


@register.filter(expects_localtime=True)
def parse_time(value, arg):
    if arg != 'NFL':
        # 2021-10-03T19:10:00Z
        date = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
        date = date + datetime.timedelta(hours=0)
        return pytz.timezone("UTC").localize(date, is_dst=True)
    elif arg == 'NFL':
        # 2021-10-03T19:10:00Z
        date = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%MZ")
        date = date + datetime.timedelta(hours=0)
        return pytz.timezone("UTC").localize(date, is_dst=True)
