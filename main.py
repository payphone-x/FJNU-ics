import datetime
import ics
import fjnu_api
import browser_cookie3
import parse

cal = ics.Calendar()

class_time = {
    "旗山校区": [None, (8, 20), (9, 15), (10, 20), (11, 15), (14, 0), (14, 55), 
	    (15, 50), (16, 45), (18, 30), (19, 25), (20, 20), (21, 15)],
    "仓山校区": [None, (8, 00), (8, 55), (10, 00), (10, 55), (14, 0), (14, 55), 
	    (15, 50), (16, 45), (18, 30), (19, 25), (20, 20), (21, 15)]
}

duration_per_class = 45

lnk = input("Link=")

suffix = parse.parse("https://jwglxt.fjnu.edu.cn/jwglxt/kbcx/xskbcx_cxXskbcxIndex.html?{}", lnk)[0]

yr = input("Year=")
st = [None, 3, 12, 16][int(input("Semester="))]

api = fjnu_api.FJNUApi(
    suffix,
    browser_cookie3.load('jwglxt.fjnu.edu.cn'),
    'xnm=%s&xqm=%d&kzlx=ck' % (yr, st)
)

print("Sending POST request...")

api.fetch()
data = api.parse()

print("Generating ics...")

week_index = 0
current_time = datetime.datetime(2022, 8, 29)

for day in range(1, 366):
    if day % 7 == 1:
        week_index += 1
    for it in data:
        campus = it['campus']
        if week_index in it['weeks'] and ((day - 1) % 7 + 1) == it['weekday_order']:
            e = ics.Event()
            e.name = it['name']
            e.begin = str(current_time + datetime.timedelta(
                hours = class_time[campus][it['class_order'][0]][0] - 8,
                minutes = class_time[campus][it['class_order'][0]][1]
            ))
            e.end = str(current_time + datetime.timedelta(
                hours = class_time[campus][it['class_order'][-1]][0] - 8,
                minutes = class_time[campus][it['class_order'][-1]][1]
            ) + datetime.timedelta(minutes=duration_per_class))
            e.location = it['location']
            e.description = it['teacher'] + ' - ' + it['class_id']
            cal.events.add(e)
    current_time += datetime.timedelta(days=1)

print("Writing output to output.ics...")

with open('output.ics', 'wb') as f:
    raw = cal.serialize()
    f.write(raw.encode('utf8'))
