import requests
import time
timing = str(int(time.time()))
url = 'https://webcast3-normal-c-lf.amemv.com/webcast/ranklist/hot/?version_code=12.7.0&pass-region=0&js_sdk_version=1.77.0.2&tma_jssdk_version=1.77.0.2&pass-route=0&app_name=aweme&app_version=12.7.0&vid=8E94A232-6D1F-40BB-99C8-DF215FE9B8B8&webcast_sdk_version=1680&device_id=53656377826&channel=App%20Store&mcc_mnc=&webcast_gps_access=1&language=zh-Hans-US&aid=1128&effect_sdk_version=7.5.0&screen_width=768&openudid=3c29e7a5160c7b6c1af8244b486188de99c61245&cdid=4D6488C3-2434-4726-A1FC-99576D168D2E&os_api=18&webcast_language=zh&ac=WIFI&os_version=13.7&webcast_locale=zh-Hans_CN&build_number=127016&device_platform=ipad&device_type=iPad%20Mini%204&is_vcd=1&iid=2955102934794942&idfa=5C0E2412-2C12-4918-A1AF-4A295AF2D6B7'
headers = {
    'Host': 'webcast3-normal-c-lf.amemv.com',
    'Connection': 'keep-alive',
    'Content-Length': '0',
    'sdk-version': '2',
    'passport-sdk-version': '5.12.1',
    'x-Tt-Token': '008c72e9add408de07eb5aaff3d6def733837ffbd575a31d7ad2690e2ed3c2950e87d92beea610ccb510a6634ff376fc8663',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Aweme 12.7.0 rv:127016 (iPad; iOS 13.7; zh-Hans_US) Cronet',
    'X-SS-STUB': 'D41D8CD98F00B204E9800998ECF8427E',
    'X-SS-DP': '1128',
    'x-tt-trace-id': '00-af7e8a6c09c7e2b59e2b8c49b89a0468-af7e8a6c09c7e2b5-01',
    'Cookie': 'odin_tt=979eceeb223d6d838bb0ac585e008d9a02d86f483c1915d66a2b39475589e33f075f9a7b51c3c680e14c6de1ee6acbd4f6a06a833ae0a13084f83a708e2c3260; d_ticket=d6f50d361ea3cf47b71df000cd04f7e5805aa; install_id=2955102934794942; ttreq=1$af7d1596ed327a65e1923f906641a671fd92da7f',
    'X-Khronos': timing,
    'X-Gorgon': '840220b8000050f0c513c9e8c6f398a271c0740eafb4fc1bbf09',
}
r = requests.post(url,headers=headers,verify=False).json()
text = r["data"]["ranks"]
for item in text:
    name = item["user"]["nickname"]
    key = item["room"]["title"]
    hot = item["score"]
    print(name,key,hot,"人气")
    print()