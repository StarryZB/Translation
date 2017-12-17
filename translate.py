from urllib import request,parse
import json

while True:
    content = input('输入翻译内容(输入q结束)：')
    if content == 'q':
        break
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com/'
    data = {'i':content,'from':'AUTO','to':'AUTO','smartresult':'dict','client':'fanyideskweb','salt':'1513172448000','sign':'e351394ea9552a065ae6cef67a63ca95','doctype':'json','version':'2.1','keyfrom':'fanyi.web','action':'FY_BY_CLICKBUTTION','typoResult':'false'}
    data = parse.urlencode(data).encode('utf-8')
    response = request.urlopen(url,data)
    html = response.read().decode('utf-8')
    target = json.loads(html)
    print('翻译结果：%s' % target['translateResult'][0][0]['tgt'])

