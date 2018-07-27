# -*- coding:utf8 -*-
import urllib.parse
import urllib.request
import urllib
import ssl
import json

ssl._create_default_https_context = ssl._create_unverified_context  # ssl 验证
host = "https://armuseum.html5.qq.com"
getMuseumList = "/api/getMuseumListV2"  # 博物馆列表api
getMuseumDetail = "/api/getMuseumDetail"  # 博物馆详情api
getShowListV2 = "/api/getShowListV2?"  # 展览数据api

headers = {
    "Accept-Encoding": "gzip",
    "content-type": "application/json",
    # "referer": "https://servicewechat.com/wx1d5046af9a8fc086/58/page-frame.html",
    "User-Agent": "Mozilla/5.0 (Linux; Android 4.4.2; MI 6  Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 MicroMessenger/6.6.7.1321(0x26060739) NetType/WIFI Language/zh_CN MicroMessenger/6.6.7.1321(0x26060739) NetType/WIFI Language/zh_CN",
    "Content-Length": 100,
    "Host": "armuseum.html5.qq.com",
    "Connection": "Keep-Alive"
}

cityIds = []  # iCityCode 列表
filePath = 'cityData'  # city数据文件


# 载入city数据
def loadCityData(filePath):
    f = open(filePath, encoding='utf-8')
    cityData = json.load(f)
    mAll = cityData['mAll']
    for key in mAll.keys():
        cityList = mAll[key]
        if cityList:
            for city in cityList:
                cityIds.append(city["iCityCode"])
    return cityIds;


# 发送HTTP请求
def httpSend(url, param="{}", type='post'):
    if type == 'post':
        postData = urllib.parse.urlencode(param).encode('utf-8')
        req = urllib.request.Request(url, postData)
    else:
        req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    res = resp.read().decode('utf-8')
    return res


def dealMuseumList(param):
    dataJson = json.loads(param)
    museumList = dataJson['vMuseum']
    return museumList


# 处理博物馆详情信息
def dealMuseumDetail(param):
    dataJson = json.loads(param)
    museumDetail = dataJson['data']
    # 更新数据库
    bCollection = museumDetail['vItemList']
    if bCollection:
        item = bCollection['vObjectItem']
        print(item)
        # 插入数据库


# 处理展览数据
def dealShow(param):
    dataJson = json.loads(param)
    showList = dataJson['vShow']
    if showList:
        for show in showList:
            print(show)
            # http 展览详情
            # 插入数据库数据


"""
1. cityId
2. 获取city下的博物馆列表
3. 博物馆详情
3. 获取博物馆下（专题，展览，精品）的物品（器皿，画）
4. 物品详情

其他：图片资源最后处理

"""
cityIds = loadCityData(filePath)
for cityid in cityIds:
    api = host + getMuseumList
    postdata = {
        "iCityCode": 440300,
        "dLatitude": 24.00125,
        "dLongitude": 100.56358,
        "eSortType": 0,
        "iPageSize": 100,
        "vContextData": ""
    }
    res = httpSend(api, postdata, "post")
    museumList = dealMuseumList(res)
    if museumList:
        for museum in museumList:
            museumId = museum["iId"]
            # post 获取博物馆详情
            api = host + getMuseumDetail
            param = {"id": museumId}
            res = httpSend(api, param, "post")
            print(res)
            dealMuseumDetail(res)

            # get 获取展览数据

            api2 = host + getShowListV2;
            displayData = httpSend(
                url="https://armuseum.html5.qq.com/api/getShowListV2?page_size=3&city_id=-1&museum_id=23332",
                type="get")
            print(displayData)
