import requests
import time
headers = {
    'Host': 'mp.weixin.qq.com',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1301.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.5 WindowsWechat',
    'X-Requested-With': 'XMLHttpRequest',
    'Accept': '*/*',
    'Referer': 'https://mp.weixin.qq.com/mp/appmsgalbum?action=getalbum&album_id=1321044729160859650&__biz=MzU2ODYzNTkwMg==&uin=MjQ2NTA4MTIxOA%3D%3D&key=3c70845fba7fea590ab059e076f3b57a8e9d9f67fa6969dcc59ef57390ab8386d099c71f93808f02f0a5f801afa1925e0c5ec97d240505db10f192bb7af821811fa20fe170e6d8b3e30ec8c0f105acf05c6475888121a35808e3ec515f36e7ba950928543de8a4cfe62c4110d31a85608376f43b349220d152409c0f99c6842d&devicetype=Windows+10+x64&version=62090529&lang=zh_CN&ascene=7&pass_ticket=xVUSh9emdB6ugyZKJyPqwMveyFfeEcmczK%2BbNDcL7TmoktjKS%2FI3BZ4IFa%2FByX6A&winzoom=1.25',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4',
    'Cookie': 'rewardsn=; wxtokenkey=777; wxuin=2465081218; devicetype=Windows10x64; version=62090529; lang=zh_CN; pass_ticket=xVUSh9emdB6ugyZKJyPqwMveyFfeEcmczK+bNDcL7TmoktjKS/I3BZ4IFa/ByX6A; wap_sid2=CILPuJcJEooBeV9ITHhWOHRyZHg1UVN1UjdHczdhYlhjMDlDSlAyQzlud3JMaXpFLXFtN1ZBMG4xV2lFbVZLWV9CMXk3MU1WQzZVeHpFTmZJd0d0all3NUpmXzNJMl9WVzNvWEw5VVlDZFFnVTBpRGFna3dvdGxLY0dvWE9pNWpXbkxJT3FxaG9wR3RCSVNBQUF+MI/JvPoFOAxAlE4=',
}
url = 'https://mp.weixin.qq.com/mp/appmsgalbum?action=getalbum&__biz=MzU2ODYzNTkwMg==&album_id=1321044729160859650&begin_msgid=2247484164&begin_itemidx=1&count=10&uin=MjQ2NTA4MTIxOA%253D%253D&key=3c70845fba7fea590ab059e076f3b57a8e9d9f67fa6969dcc59ef57390ab8386d099c71f93808f02f0a5f801afa1925e0c5ec97d240505db10f192bb7af821811fa20fe170e6d8b3e30ec8c0f105acf05c6475888121a35808e3ec515f36e7ba950928543de8a4cfe62c4110d31a85608376f43b349220d152409c0f99c6842d&pass_ticket=xVUSh9emdB6ugyZKJyPqwMveyFfeEcmczK%25252BbNDcL7TmoktjKS%25252FI3BZ4IFa%25252FByX6A&wxtoken=&devicetype=Windows%26nbsp%3B10%26nbsp%3Bx64&clientversion=62090529&__biz=MzU2ODYzNTkwMg%3D%3D&appmsg_token=1076_qr8FudbtoNZ%252BJGgYPZLSISVGyIJaPOsHN0vhow~~&x5=0&f=json'
res = requests.get(url,headers=headers,verify=False).json()
tt = res["getalbum_resp"]["article_list"]
for item in tt:
    title = item["title"]
    link = item["url"]
    print("title:",title,"link:",link,)
    time.sleep(1)