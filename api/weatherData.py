import requests
# elementChineseName={
#     'Wx':'天氣現象',
#     'MaxT':'最高溫度',
#     'MinT':'最低溫度',
#     'CI':'舒適度',
#     'PoP':'降雨機率'
# }
# elementUnit={
#     'Wx':'',
#     'MaxT':'°C',
#     'MinT':'°C',
#     'CI':'',
#     'PoP':'%'
# }

locationName = input("請輸入欲查詢的縣市名稱:")

elementChineseName=[
    '天氣現象',
    '降雨機率',
    '最低溫度',
    '舒適度',
    '最高溫度'
    
]

elementUnit=[
    '',
    '%',
    '°C',
    '',
    '°C'
]
    
url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001"

parameters = {
    'Authorization':"CWB-111EAC52-3B14-46FE-A793-4081D3E0576D",
    'locationName':locationName
}

response = requests.get(url, params=parameters)

if response.status_code == 200:
    data = response.json()
    for location in data['records']['location']:
        print(location['locationName'])
        for time in range(len(location['weatherElement'][0]['time'])):
            print(f"startTime:{location['weatherElement'][0]['time'][time]['startTime']}")
            print(f"endTime:{location['weatherElement'][0]['time'][time]['endTime']}")
            for i in range(5):
                print(f"{elementChineseName[i]}:{location['weatherElement'][i]['time'][time]['parameter']['parameterName']}{elementUnit[i]}")
            print()    
else:
    print('error!')