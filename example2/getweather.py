# -*- coding: utf-8 -*-


#http://api.map.baidu.com/telematics/v2/weather?location=城市名称&ak=密匙

import pyquery as pq
import urllib
import sys
import json

ENCODING = 'utf-8'


def queryLocation(term):
    ak = "hOT0ar9OmTdSk2yAsVhOChnN"
    term = term.encode(ENCODING) if type(term) == unicode else term
    url = "http://api.map.baidu.com/telematics/v2/weather?output=json&location=" + urllib.quote(term) + "&ak=" + ak
    resp = urllib.urlopen(url)
    data = resp.read()
    data = json.loads(data)
    # print data
    if not data or data["status"] != 'success':
        print u"找不到地点".encode(ENCODING)

    temp = data["results"][0]["temperature"]
    weather = data["results"][0]["weather"]
    date = data["results"][0]["date"]
    # print date + " " + temp + " " + weather
    return date + " " + temp + " " + weather
    # for d in data["i"]:
    #     code = d['i']
    #     break
    # return code

def queryRealTimeWeatherInfo(code):
    #url = "http://m.weather.com.cn/data/%s.html" % code
    url = "http://www.weather.com.cn/data/sk/%s.html" % code
    resp = urllib.urlopen(url)
    data = json.load(resp)
    if not data:
        print u"天气预报还没出来".encode(ENCODING)
    return data['weatherinfo']

def showRealTimeWeatherInfo(info):
    template = u"{city} {time} 天气实况: 气温{temp}℃, {WD}{WS}, 湿度{SD}"
    print template.format(**info).encode(ENCODING)


def main():
    assert len(sys.argv) >= 3
    function = sys.argv[1]
    term = ''.join(sys.argv[2:])
    if function == 'realtime':
        # 实时
        # showRealTimeWeatherInfo(queryRealTimeWeatherInfo(queryLocation(term)))
        queryLocation(term)
if __name__ == '__main__':
    print queryLocation(u"北京")
    # main()
