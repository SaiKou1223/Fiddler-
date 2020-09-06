import requests
import pdfkit
import json
import time
path_wkthmltopdf = r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
headers = {
    'Host': 'mp.weixin.qq.com',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1301.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.5 WindowsWechat',
    'X-Requested-With': 'XMLHttpRequest',
    'Accept': '*/*',
    'Referer':'https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzU2ODYzNTkwMg==&scene=124&uin=MjQ2NTA4MTIxOA%3D%3D&key=70727d372177c265e00eb6821d80477fa46daa6c305bc465e93e76bceaff4034ddd3ecf4bf49ea518b7df8d742b9cdce8f3bf06d75934800fe09871be15b53633420b13dc41b0a2cdd388882d58a98e77308be7e42ac4cd4d1c5dd2cfb1479092831543fab673ee9e26ba718b060ffc7f7977ed142e7f875e747ecb6700e411a&devicetype=Windows+10+x64&version=62090529&lang=zh_CN&a8scene=7&pass_ticket=TuM7MyzfZ8LGcoLMMGgIFSggpmxs5%2FNf%2F%2Fqm2GRQKBGDPBk9ALnMmg1PpC7hvmei&winzoom=1.25',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4',
    'Cookie': 'rewardsn=; wxtokenkey=777; wxuin=2465081218; devicetype=android-29; version=27001237; lang=zh_CN; pass_ticket=0sEmGkvdUUgFTyNvuwvBlGMCQWi4pAI5OoVwtexQ4u4fZfPEiGz4SKJ5xcjdCy4; wap_sid2=CILPuJcJEooBeV9IRnRWZVN2MkdBTVFhTHF1N2dZZm5wbU5VWHlmM0Nvc2FBRkRqbVhpbnFBSTJ3ZzljYWhKSFRWaFhiUU82OFMyZnJkVi1UZGE4N0NfNmNnR2NCcElkc2lta3lPVnlwanVsaU9IbERYOHg0aGpZZlhuNmRRZ1QzUHFiVlp0ZkZQNklSSVNBQUF+MIeJv/oFOA1AlU4='
}
url = 'https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MzU2ODYzNTkwMg==&f=json&offset=15&count=10&is_ok=1&scene=124&uin=MjQ2NTA4MTIxOA%3D%3D&key=70727d372177c265ae9ca6cc54b73ccaa6e20d0c73302e9e55c0cfb1a7a1da0d8b0bc29bd709568edb561fd1a8137d29f7f8b59057e6ea69a1c9c40296e77bc6217156c86655025b0c5ee187b4f71842d47f65ff814e36b75a4247efc5d83f66c77bac83d04a5275616f0b8d70e01611bd87b1567e1f5e0e4cd2c3eb89b434a7&pass_ticket=0sEmGkvdUUgFTyNvuwvBlGMCQW%2Bi4pAI5OoVwtexQ4u4fZfPEiGz4SKJ5xcjdCy4&wxtoken=&appmsg_token=1077_BuNKl7lGkuaHDWk%252BbphLQEAtSett706DZutapQ~~&x5=0&f=json'
res = requests.get(url,headers=headers,verify=False).json()
text = res["general_msg_list"]
tt = json.loads(text)["list"]
for x in range(len(tt)):
    title = tt[x]["app_msg_ext_info"]["title"]
    url = tt[x]["app_msg_ext_info"]["content_url"]
    pdfkit.from_url(url, '/TEST/wechat/{}.pdf'.format(title),configuration=config)
    print("正在下载title:",title,"link:",url,)
    time.sleep(1)
