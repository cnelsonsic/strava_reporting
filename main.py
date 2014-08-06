#!/usr/bin/env python
import datetime
from dateutil.relativedelta import relativedelta

from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

from stravalib import unithelper
from stravalib.client import Client

from access_token import ACCESS_TOKEN

client = Client(access_token=ACCESS_TOKEN)
athlete = client.get_athlete()
start_date = datetime.date.today()+relativedelta(months=-1)
activities = client.get_activities(after=start_date)
activities_list = []
for activity in activities:
    if activity.start_date.date().month != start_date.month:
        continue
    date = activity.start_date.date().isoformat()
    distance = activity.distance
    duration = activity.elapsed_time.total_seconds()/60
    activity_type = activity.type
    activity_string = "{activity_type} for {duration:.1f} minutes ({distance:.2f} miles)".format(
        activity_type=activity_type,
        duration=duration,
        distance=unithelper.miles(activity.distance).num,
    )

    activities_list.append((date, activity_string, activity.name))

employee_name = ' '.join((athlete.firstname, athlete.lastname))
month = start_date.strftime("%B")
report = template.render(employee_name=employee_name,
                month=month,
                activities=activities_list)

filename = "Fitness form for {} {}.html".format(employee_name, month)
with open(filename, "wb") as fh:
    fh.write(report)

print "Report written to", filename
