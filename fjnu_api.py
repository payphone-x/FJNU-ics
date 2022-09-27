import requests
import json
import parse
import browser_cookie3 as bc
import re

class_time = {
    "旗山校区": [None, (8, 20), (9, 15), (10, 20), (11, 15), (14, 0), (14, 55),
             (15, 50), (16, 45), (18, 30), (19, 25), (20, 20), (21, 15)],
    "仓山校区": [None, (8, 00), (8, 55), (10, 00), (10, 55), (14, 0), (14, 55),
             (15, 50), (16, 45), (18, 30), (19, 25), (20, 20), (21, 15)]
}


class FJNUApi:
    def requirements():
        return ["link", "year", "semester"]

    def fetch(args):
        url_suffix = parse.parse(
            "https://jwglxt.fjnu.edu.cn/jwglxt/kbcx/xskbcx_cxXskbcxIndex.html?{}", args['link'])[0]
        header = {
            "Host": "jwglxt.fjnu.edu.cn",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
            "Origin": "https://jwglxt.fjnu.edu.cn",
            "Referer": "https://jwglxt.fjnu.edu.cn/jwglxt/kbcx/xskbcx_cxXskbcxIndex.html?layout=default&" + url_suffix,
        }
        semester = [None, 3, 12, 16][int(args['semester'])]

        res = requests.post(
            'https://jwglxt.fjnu.edu.cn/jwglxt/kbcx/xskbcx_cxXsgrkb.html?' + url_suffix,
            headers=header,
            data='xnm=%s&xqm=%d&kzlx=ck' % (args['year'], semester),
            cookies=bc.load('jwglxt.fjnu.edu.cn')
        )

        content = json.loads(res.content)['kbList']
        res = []
        
        for it in content:
            _ = parse.parse("{}-{}", it['jcs'])
            _class = [int(_[0]), int(_[1])]
            campus = it['xqmc']

            _weeks = []
            for s in it['zcd'].split(','):
                s = s.strip()
                if re.search("\d*-\d*周", s):
                    _ = parse.parse("{}-{}周", s)
                    for i in range(int(_[0]), int(_[1]) + 1):
                        _weeks.append(i)
                elif re.search("\d*周", s):
                    _ = parse.parse("{}周", s)
                    _weeks.append(int(_[0]))

            # 写后端的傻逼我囸你妈

            res.append({
                "name": it['kcmc'],
                "teacher": it['xm'],
                "location": it['cdmc'],
                "time": {
                    "from": (class_time[campus][_class[0]][0], class_time[campus][_class[0]][1]),
                    "to": (class_time[campus][_class[1]][0], class_time[campus][_class[1]][1])
                },
                "weeks": _weeks,
                "weekday_order": int(it['xqj']),
                "class_order": _class
            })
        return res
