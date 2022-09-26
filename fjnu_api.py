import requests
import json
import parse

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
            _weeks = parse.parse("{}-{}周", it['zcd'])
            if _weeks != None:
                _weeks = [ int(i) for i in range(int(_weeks[0]), int(_weeks[1]) + 1) ]
            else:
                _weeks = [ int(parse.parse("{}周", it['zcd'])[0]) ]
            # 我囸你妈
            res.append({
                "name": it['kcmc'],
                "teacher": it['xm'],
                "mandatory": True,
                "weeks_str": it['zcd'],
                "location": it['cdmc'],
                "class_id": it['cd_id'],
                "weeks": _weeks,
                "weekday_order": int(it['xqj']),
                "class_order": _class
            })
        return res