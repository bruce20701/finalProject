import requests
from datetime import datetime

#輸入時間以獲取這時間臺北市的天氣狀況
def qureyNearestTimeWeather(searchTime):

    url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001"

    locationName = "臺北市"

    parameters = {
    'Authorization':"CWB-111EAC52-3B14-46FE-A793-4081D3E0576D",
    'locationName':locationName
    }

    response = requests.get(url, params=parameters)

    if response.status_code == 200:
        data = response.json()

        #取得特定城市的天氣(搜尋單一城市，所以只list內只有第0項)
        location = data['records']['location'][0]

        i=0
        weatherInit = []

        #利用weatherElement中的第0項Wx中的time取得startTime
        for time in location['weatherElement'][0]['time']:

            #切出H:M
            selectedTime = time['startTime'][-8:-3]


            if(selectedTime > searchTime):
                for j in range(5):
                    weatherInit.append(location['weatherElement'][j]['time'][i]['parameter']['parameterName'])
                return weatherInit
            else:
                i+=1
    else:
        print("error!")

#輸入城市以獲取六小時後的天氣狀況
def qureyWeatherbyCity(locationName):

    url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001"

    parameters = {
    'Authorization':"CWB-111EAC52-3B14-46FE-A793-4081D3E0576D",
    'locationName':locationName
    }

    response = requests.get(url, params=parameters)

    if response.status_code == 200:
        data = response.json()

        #獲取當前時間
        searchTime = datetime.now().strftime("%H%M")

        
        #取得特定城市的天氣(搜尋單一城市，所以只list內只有第0項)
        location = data['records']['location'][0]

        i=0
        weatherInit = []

        #利用weatherElement中的第0項Wx中的time取得endTime
        for time in location['weatherElement'][0]['time']:

            #切出H:M:S
            selectedTime = time['endTime'][-8:-3]

            #判斷時間區段
            
            if(selectedTime > searchTime):
                for j in range(5):
                    weatherInit.append(location['weatherElement'][j]['time'][i]['parameter']['parameterName'])
                return weatherInit
            else:
                i+=1
    else:
        print("error!")