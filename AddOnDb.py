import requests
import random
from datetime import datetime

#Adding data to QuestDB

success = 0
fail = 0
random.seed()
for x in range(1000):
    temp = random.randint(-40, 55)
    rain24H = round(random.uniform(10.45, 235.15), 2)
    thunder = bool(random.getrandbits(1))
    query = "insert into weather values("\
        + str(temp) + ","\
        + str(rain24H) + "," \
        + str(thunder) +",systimestamp())"
    r = requests.get("http://localhost:9000/exec?query=" + query)
    if r.status_code == 200:
        success += 1
    else:
        fail += 1
    
print("Rows inserted: " + str(success))
if fail > 0:
    print("Rows Failed: " + str(fail))