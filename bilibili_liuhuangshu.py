import requests
import re
from  urllib import request
headers = {
    'Host':'app.bilibili.com',
    'Connection':'keep-alive',
    'User-Agent':'bili-universal/10230CFNetwork/1128.0.1Darwin/19.6.0os/iosmodel/iPadmini4mobi_app/iphonebuild/10230osVer/13.6network/2channel/AppStore',
    'APP-KEY':'iphone',
    'Buvid':'ee3298d6de1c2a13cd9a43481efc0e00',
    'ENV':'prod',
    'Cookie':'PVID=3;_uuid=C1B88613-07BB-632C-32F4-43987965AF8936284infoc;buvid3=F4B2CE3B-AC9C-4D6B-8143-8855AD28C9D0155818infoc;Buvid=ee3298d6de1c2a13cd9a43481efc0e00;DedeUserID=272059235;DedeUserID__ckMd5=c417fc1066750971;SESSDATA=4e2cfb10%2C1601120167%2C0acdcc81;bili_jct=1cb7028f4460988e3c0b4417b4c875c7;sid=5okmu4bl;bfe_id=61a513175dc1ae8854a560f6b82b37af',
}
url = 'https://app.bilibili.com/x/v2/search?access_key=297c35e4013cbab37e21e82e5f174981&actionKey=appkey&appkey=27eb53fc9058f8c3&build=10230&device=pad&duration=0&fnval=16&fnver=0&fourk=0&from_source=app_search&highlight=1&is_org_query=0&keyword=%E5%88%98%E7%9A%87%E5%8F%94&local_time=8&mobi_app=iphone&order=default&platform=ios&pn=1&ps=20&qn=80&recommend=1&rid=0&s_locale=zh-Hans_US&sign=0dd7b853ae2beb4c298204310204de57&statistics=%7B%22appId%22%3A1%2C%22version%22%3A%226.8.1%22%2C%22abtest%22%3A%22%22%2C%22platform%22%3A2%7D&ts=1599441593'
res = requests.get(url,headers=headers,verify=False).json()
# url = 'GET https://app.bilibili.com/x/v2/search?access_key=297c35e4013cbab37e21e82e5f174981&actionKey=appkey&appkey=27eb53fc9058f8c3&build=10230&device=pad&duration=0&fnval=16&fnver=0&fourk=0&from_source=app_search&highlight=1&is_org_query=0&keyword=%E5%88%98%E7%9A%87%E5%8F%94&local_time=8&mobi_app=iphone&order=default&platform=ios&pn={}&ps=20&qn=80&recommend=1&rid=0&s_locale=zh-Hans_US&sign=0dd7b853ae2beb4c298204310204de57&statistics=%7B%22appId%22%3A1%2C%22version%22%3A%226.8.1%22%2C%22abtest%22%3A%22%22%2C%22platform%22%3A2%7D&ts=1599441593'
# https://app.bilibili.com/x/v2/search?access_key=297c35e4013cbab37e21e82e5f174981&actionKey=appkey&appkey=27eb53fc9058f8c3&build=10230&device=pad&duration=0&fnval=16&fnver=0&fourk=0&from_source=app_search&highlight=1&is_org_query=0&keyword=%E5%88%98%E7%9A%87%E5%8F%94&local_time=8&mobi_app=iphone&order=default&platform=ios&pn=1&ps=20&qn=80&recommend=1&rid=0&s_locale=zh-Hans_US&sign=0dd7b853ae2beb4c298204310204de57&statistics=%7B%22appId%22%3A1%2C%22version%22%3A%226.8.1%22%2C%22abtest%22%3A%22%22%2C%22platform%22%3A2%7D&ts=1599441593
# https://app.bilibili.com/x/v2/search?access_key=297c35e4013cbab37e21e82e5f174981&actionKey=appkey&appkey=27eb53fc9058f8c3&build=10230&device=pad&duration=0&fnval=16&fnver=0&fourk=0&from_source=app_search&highlight=1&is_org_query=0&keyword=%E5%88%98%E7%9A%87%E5%8F%94&local_time=8&mobi_app=iphone&order=default&platform=ios&pn=2&ps=20&qn=80&recommend=1&rid=0&s_locale=zh-Hans_US&sign=2245fe9e01fc7a0c25c60d878d3fbe1a&statistics=%7B%22appId%22%3A1%2C%22version%22%3A%226.8.1%22%2C%22abtest%22%3A%22%22%2C%22platform%22%3A2%7D&ts=1599441637
tt = res["data"]["items"]["archive"]
for item in tt:
    title = item["title"]
    author  = item["author"]
    jpg_url = item["cover"]
    url = item["uri"]
    title = re.sub(r'[\/em\?？\，,。！!【】<《> 》….：:“”]', '', title)
    title = re.sub(r'[class="kyword"]', '', title)
    print("title:",title,"author:",author,"jpg:",jpg_url,"url:",url,)
    request.urlretrieve(jpg_url,'D:\\testfile\\{}.jpg'.format(title))