import requests

APP_ID = "d2cf859ed41ccee36293a47f254288a72e535670"
API_URL  = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

#データの種類：国勢調査
#内容：15歳以上の労働人口、失業者人口、非労働人口の人数、割合
#エンドポイント： https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData
params = {
    "appId": APP_ID,
    "statsDataId":"0003412175",
    "cdArea":"12101,12102,12103,12104,12105,12106",
    "cdCat01": "A1101",
    "metaGetFlg":"Y",
    "cntGetFlg":"N",
    "explanationGetFlg":"Y",
    "annotationGetFlg":"Y",
    "sectionHeaderFlg":"1",
    "replaceSpChars":"0",
    "lang": "J"  # 日本語を指定
}



#response = requests.get(API_URL, params=params)
response = requests.get(API_URL, params=params)
# Process the response
data = response.json()
print(data)
