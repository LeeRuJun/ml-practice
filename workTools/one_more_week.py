# -*- coding: UTF-8 -*-

import json

import requests
import simplejson as simplejson

url = 'http://10.28.158.111:8080/api/completeUploadVideo'


def go():
    f = open('test.txt', encoding='utf-8')
    for content in f:
        content = content.strip()
        a = content.split(',')
        paramFormat = '{"vid":%s,"name":"String","origAddr":"String","type":"String","userDefined":"shortvideoid=%s"}' % (a[0], a[1]);
        print(paramFormat)
        # param = json.dumps(paramFormat, ensure_ascii=False).encode("utf-8")
        r = requests.post(url, data=paramFormat)
        dic = simplejson.loads(r.content)
        print(dic)

    # paramOrigin = '{"head":{"syscode":"String","lang":"String","auth":"String","cid":"String","ctok":"String","cver":"String","sid":"String","extension":[{"name":"uid","value":"JSYF_JP_KFCS_38179"}],"sauth":"String"},"title":"三皇寨","isPrivate":true,"poiID":86142,"durationSecond":967,"videoSpaceInBytes":24,"appFormatFailure":0,"coverImageUrl":"","shortVideoID":0,"coverImageSource":0,"sourceCoverImageID":"String"}'
    # param = json.dumps(paramOrigin, ensure_ascii=False).encode("utf-8")
    # r = requests.post(url, data=param)
    # dic = simplejson.loads(r.content)
    # print(dic)


go()
