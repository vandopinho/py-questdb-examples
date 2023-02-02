import requests
import io
import pandas as pd


#Query data from QuestDB

r = requests.get("http://localhost:9000/exp?query=select * from weather")
rawData = r.text
print(rawData)


#Convert raw output to DataFrame

pData = pd.read_csv(io.StringIO(rawData), parse_dates=['timestamp'])
print(pData)

