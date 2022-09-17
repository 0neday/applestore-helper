#!/usr/bin/python

import requests
import json
import asyncio
from requests.structures import CaseInsensitiveDict

# http get
url = 'https://www.apple.com.cn/shop/fulfillment-messages'
storeCode = 'R532'
#model = 'MQ1C3CH/A'
model = 'MQ0M3CH/A'
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["user-agent"] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'

# dingtalk for appstore helper
dingtalkUrl = 'https://oapi.dingtalk.com/robot/send?access_token='
token = 'yourdingtalk_accesskey'
headers["Content-Type"] = "application/json"

# flag
flag = 1

# get status
async def get_status():
    getStock = json.loads(requests.get(url + '?searchNearby=true&pl=true&mts.0=regular&mts.1=compact&parts.0=' + model + '&store=' + storeCode, headers=headers).content)
    storeList = getStock['body']['content']['pickupMessage']['stores']
    for x in range(len(storeList)):
        status = storeList[x]['partsAvailability'][model]['pickupDisplay']
        if status == 'available':
#            global flag
#            flag = 0
            product = storeList[x]['partsAvailability'][model]['messageTypes']['compact']['storePickupProductTitle']
            productList = product.split()
            message = storeList[x]['storeName'] + ': ' + productList[4] + ' ' + productList[3] + ', ' + storeList[x]['partsAvailability'][model]['pickupSearchQuote']
            payload = { "msgtype": "text","text": {"content": message},  "at": {"isAtAll": 0} }
            requests.post(url=dingtalkUrl + token, data=json.dumps(payload), headers=headers)
            print(message)

async def main():
    while flag:
        asyncio.ensure_future(get_status())
        await asyncio.sleep(3)

asyncio.run(main())


