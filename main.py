import datetime
import ics
import fjnu_api
import browser_cookie3
import parse

cal = ics.Calendar()

duration_per_class = datetime.timedelta(minutes=45)

args = {}

for key in fjnu_api.FJNUApi.requirements():
    args[key] = input(key + '=')

print("Sending POST request...")

data = fjnu_api.FJNUApi.fetch(args)

print("Generating ics...")

week_index = 0
current_time = datetime.datetime(2022, 8, 29)

for day in range(1, 366):
    if day % 7 == 1:
        week_index += 1
    for it in data:
        if week_index in it['weeks'] and ((day - 1) % 7 + 1) == it['weekday_order']:
            e = ics.Event()
            e.name = it['name']
            e.begin = str(current_time + datetime.timedelta(
                hours = it['time']['from'][0] - 8,
                minutes = it['time']['from'][1]
            ))
            e.end = str(current_time + datetime.timedelta(
                hours = it['time']['to'][0] - 8,
                minutes = it['time']['to'][1]
            ) + duration_per_class)
            e.location = it['location']
            e.description = '授课教师: ' + it['teacher']
            cal.events.add(e)
    current_time += datetime.timedelta(days=1)

print("Writing output to output.ics...")

with open('output.ics', 'wb') as f:
    raw = cal.serialize()
    f.write(raw.encode('utf8'))
