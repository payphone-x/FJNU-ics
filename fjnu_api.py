import requests
import json
import parse
import re

class FJNUApi:
    def __init__(this, url_suffix, cookie, body):
        this.url = 'https://jwglxt.fjnu.edu.cn/jwglxt/kbcx/xskbcx_cxXsgrkb.html?' + url_suffix
        this.body = body
        this.content = {}
        this.headers = {
            "Host": "jwglxt.fjnu.edu.cn",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
            "Origin": "https://jwglxt.fjnu.edu.cn",
            "Referer": "https://jwglxt.fjnu.edu.cn/jwglxt/kbcx/xskbcx_cxXskbcxIndex.html?layout=default&" + url_suffix,
        }
        this.cookies = cookie

    def fetch(this):
        res = requests.post(this.url, headers=this.headers, data=this.body, cookies=this.cookies)
        raw = res.content
        this.content = json.loads(raw)['kbList']

    def parse(this):
        res = []
        for it in this.content:
            _class = parse.parse("{}-{}", it['jcs'])
            _class = list(range(int(_class[0]), int(_class[1]) + 1))
            _weeks = []
            for s in it['zcd'].split(','):
                s = s.strip()
                if re.search("\d*-\d*周",s):
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
                "mandatory": True,
                "weeks_str": it['zcd'],
                "location": it['cdmc'],
                "class_id": it['cd_id'],
                "weeks": _weeks,
                "weekday_order": int(it['xqj']),
                "class_order": _class,
                "campus": it['xqmc']
            })
        return res