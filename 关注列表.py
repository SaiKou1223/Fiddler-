import requests
url = 'https://api3-normal-c-lf.amemv.com/aweme/v1/user/following/list/?tma_jssdk_version=1.77.0.2&ac=WIFI&vcd_count=0&sec_user_id=MS4wLjABAAAAOcbHCrK8BdwHIU6kUmPuFI1s5G5yekK8RAYJQY9OtBc&address_book_access=1&source_type=1&offset=0&count=80&gps_access=3&user_id=77873695181&vcdAuthFirstTime=0&user_avatar_shrink=96_96&max_time=1599737119&'
# https://api3-normal-c-lf.amemv.com/aweme/v1/user/following/list/?tma_jssdk_version=1.77.0.2&ac=WIFI&vcd_count=0&sec_user_id=MS4wLjABAAAAOcbHCrK8BdwHIU6kUmPuFI1s5G5yekK8RAYJQY9OtBc&address_book_access=1&source_type=1&offset=0&count=count&gps_access=3&user_id=77873695181&vcdAuthFirstTime=0&user_avatar_shrink=96_96&max_time=1599737119&
headers = {
    'Host':'api3-normal-c-lf.amemv.com',
    'Connection':'keep-alive',
    'sdk-version':'2',
    'passport-sdk-version':'5.12.1',
    'x-Tt-Token':'0087e0c2b8324da2f230e1d01749cddc93d1bf3a45dc33bf691ecc423925b3593f53e7bb71d0a5250c08b4b3e1556b44695',
    'User-Agent':'Aweme12.5.0rv:125009(iPad;iOS13.7;zh-Hans_US)Cronet',
    'X-SS-DP':'1128',
    'x-tt-trace-id':'00-77c4c8d309c7e2b59e2dbc6ae5cd0468-77c4c8d309c7e2b5-01',
    # 00-77cbca3e09c7e2b59e2ee41c1a400468-77cbca3e09c7e2b5-01
    'Cookie':'d_ticket=d6f50d361ea3cf47b71df000cd04f7e5805aa;odin_tt=388f6150d29f448f1c4a8c36180db8536e04505905400c44cf2544f443202220de7703a42a5c6745e8ae3f30a4fd88d5;sessionid=87e0c2b8324da2f230e1d01749cddc93;sessionid_ss=87e0c2b8324da2f230e1d01749cddc93;sid_guard=87e0c2b8324da2f230e1d01749cddc93%7C1597827019%7C5182807%7CSun%2C+18-Oct-2020+08%3A30%3A26+GMT;sid_tt=87e0c2b8324da2f230e1d01749cddc93;uid_tt=941ba20f228b76b548539ab2dde17da9;uid_tt_ss=941ba20f228b76b548539ab2dde17da9;install_id=52384865466423;ttreq=1$9fff6352a1a9dfe3f6e8f25a67fd4cab9693a888',
    'X-Khronos':'1599737218',
    'X-Gorgon':'8402e0cb000083d34b07213f7b321c34fc0e1ed8eb3eeef2435f',
    # 840280fc0000f6a6eb3544d7ea45d4a42ce56e9bc17398e5d4bf
    'x-common-params-v2':'channel=App%20Store&version_code=12.5.0&app_name=aweme&vid=8E94A232-6D1F-40BB-99C8-DF215FE9B8B8&app_version=12.5.0&mcc_mnc=&device_id=53656377826&aid=1128&screen_width=1536&openudid=3c29e7a5160c7b6c1af8244b486188de99c61245&os_api=18&os_version=13.7&device_platform=ipad&build_number=125009&device_type=iPad5,1&iid=615336558996375&idfa=F2CF732E-1A7C-402B-803C-1C0596D1ACD9&js_sdk_version=1.77.0.2&cdid=4D6488C3-2434-4726-A1FC-99576D168D2E',
}
res = requests.get(url,headers=headers,verify=False).json()
tt = res["followings"]
for item in tt:
    name = item['nickname']
    print(name)