#利用データ：東京都オープンデータ「自転車駐車場（駐輪場）情報」
#データ形式：CSV
#取得URL：https://www.opendata.metro.tokyo.lg.jp/suisyoudoukou/csv/bicycle_parking.csv

import requests
import pandas as pd

#CSVのURL
CSV_URL = "https://www.opendata.metro.tokyo.lg.jp/suisyoudoukou/csv/bicycle_parking.csv"

#CSVデータを取得し、エンコーディングをUTF-8に明示
response = requests.get(CSV_URL)
response.encoding = "utf-8"  # 日本語対応

#CSV読み込み
df = pd.read_csv(pd.compat.StringIO(response.text))

# データの先頭5行を表示
print("--- 東京都自転車駐車場データ（先頭5件)---")
print(df.head())
