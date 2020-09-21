import requests
headers = {
    'Host': 'api3-normal-c-lf.amemv.com',
    'Connection': 'keep-alive',
    'sdk-version': '2',
    'passport-sdk-version': '5.12.1',
    'x-Tt-Token': '0087e0c2b8324da2f230e1d01749cddc93915c7340d39b4c92b690e54b283c6c56cf72f2433aa64aea238fdd59f7c40700e',
    'User-Agent': 'Aweme 12.4.0 rv:124013 (iPad; iOS 13.6; zh-Hans_US) Cronet',
    'X-SS-DP': '1128',
    'x-tt-trace-id': '00-53c3d74609c7e2b59e22844356c80468-53c3d74609c7e2b5-01',
    'Cookie': 'd_ticket=d6f50d361ea3cf47b71df000cd04f7e5805aa; odin_tt=388f6150d29f448f1c4a8c36180db8536e04505905400c44cf2544f443202220de7703a42a5c6745e8ae3f30a4fd88d5; sessionid=87e0c2b8324da2f230e1d01749cddc93; sessionid_ss=87e0c2b8324da2f230e1d01749cddc93; sid_guard=87e0c2b8324da2f230e1d01749cddc93%7C1597827019%7C5182807%7CSun%2C+18-Oct-2020+08%3A30%3A26+GMT; sid_tt=87e0c2b8324da2f230e1d01749cddc93; uid_tt=941ba20f228b76b548539ab2dde17da9; uid_tt_ss=941ba20f228b76b548539ab2dde17da9; install_id=52384865466423; ttreq=1$9fff6352a1a9dfe3f6e8f25a67fd4cab9693a888',
    'X-Khronos': '1599133176',
    'X-Gorgon': '8402a01d0000be916ce5edaf2178adde5e80045bdd4c1595714d',
}
url = 'https://api3-normal-c-lf.amemv.com/aweme/v1/hot/search/list/?version_code=12.4.0&js_sdk_version=1.75.0.7&tma_jssdk_version=1.75.0.7&app_name=aweme&app_version=12.4.0&vid=8E94A232-6D1F-40BB-99C8-DF215FE9B8B8&device_id=53656377826&channel=App%20Store&mcc_mnc=&aid=1128&screen_width=1536&openudid=3c29e7a5160c7b6c1af8244b486188de99c61245&cdid=4D6488C3-2434-4726-A1FC-99576D168D2E&os_api=18&ac=WIFI&os_version=13.6&build_number=124013&device_platform=ipad&device_type=iPad5,1&is_vcd=1&iid=52384865466423&idfa=F2CF732E-1A7C-402B-803C-1C0596D1ACD9&words_in_panel=&trend_entry_word=&current_word=&source=0&mac_address=02%3A00%3A00%3A00%3A00%3A00&detail_list=1'
res = requests.get(url,headers=headers).json()
items = res["data"]["word_list"]
for item in items:
    title = item["word"]
    print("title:",title)