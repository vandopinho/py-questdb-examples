import aiohttp
import asyncio
import time
import random
import requests

start_time = time.time()
random.seed()
 

temp = random.randint(-40, 55)
rain24H = round(random.uniform(10.45, 235.15), 2)
thunder = bool(random.getrandbits(1))

query = "insert into weather values("\
        + str(temp) + ","\
        + str(rain24H) + "," \
        + str(thunder) +",systimestamp())"

async def insert_db(session, url):
    async with session.get(url + query) as resp:
        return resp.status

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for number in range(1, 2000):
            url_temp = "http://localhost:9000/exec?query="
            tasks.append(asyncio.ensure_future(insert_db(session, url_temp)))
        insertedTemp = await asyncio.gather(*tasks)

asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))

