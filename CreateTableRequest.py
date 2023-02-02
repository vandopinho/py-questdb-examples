import requests
import urllib.parse as par

#Creating a Database in QuestDB

q = 'create table weather'\
    '(temp int,'\
    'rain24H double,'\
    'thunder boolean,'\
    'timestamp timestamp)'\
    'timestamp(timestamp)'
r = requests.get("http://localhost:9000/exec?query=" + q)
print(r.status_code)