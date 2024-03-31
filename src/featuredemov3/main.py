from featuredemov3.features.sms import get_feature_sms
from featuredemov3.features.loan import get_feature_loan3
from featuredemov3.features.calllog import get_features_call_v2
from featuredemov3.features.app import get_features_app
from typing import Union
from fastapi import FastAPI, Request
import time
import random
import threading
import asyncio

import sys
print(sys.path)


app = FastAPI()


@app.get("/")
async def read_root():
    print("Sleeping main thread: ", threading.get_ident())
    results = await time_consuming_func()
    return results


@app.post("/data")
async def get_data(request: Request):
    # print(vars(request))
    data = await request.json()

    print(data)

    fgroup = data['fgroup'][0]

    features = {}

    if fgroup == 'sms_v1':
        features = await get_feature_sms()

    if fgroup == 'loan3_un':
        features = await get_feature_loan3()

    if fgroup == 'app_v1':
        features = await get_features_app()

    if fgroup == 'call_v2':
        features = await get_features_call_v2()

    await asyncio.sleep(5)

    return {"code": "0000", "data": features}


@app.get("/ping")
async def ping():
    # print(request.client)
    print("Hello")
    await asyncio.sleep(5)
    print("bye")
    return "pong"


async def time_consuming_func():
    print("Sleeping inside for 10 seconds, thread: ", threading.get_ident())
    # time.sleep(10)
    await asyncio.sleep(3)
    print("wake up")
    return {"Hello": "World", "random": random.randint(1, 100)}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
