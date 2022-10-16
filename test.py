import string
import requests
import json

url='https://dev.bees-kconnect.com/'

postTokenPath = 'eai/extras/common_keai_0001'
getOrderPath = 'eai/orders/ORDER_KBON_0003'

postTokenHeader = { "Accept" : "*/*", "Content-Type" : "application/json", "Authorization" : "Basic ZWFpX2tib246ZWFpX2tib25Ab2IuY28ua3I=", "country" : "KR", "timezone" : "Asia/Seoul" }
postTokenBody = { "POC_ID":"2148665741", "WS_ID":"2148665741" }

tokenJson = json.loads(requests.post(url+postTokenPath, headers=postTokenHeader, json=postTokenBody).text)

bearerToken = 'Bearer ' + tokenJson['token']

getOrderHeader = { "Accept" : "*/*", "Content-Type" : "application/json", "country" : "KR", "timezone" : "Asia/Seoul", "payload-param" : "?orderStatus=PLACED&page=1&pageSize=2&country=KR&vendorId=\"5148108927\"", "Authorization" : bearerToken }

orderJson = json.loads(requests.get(url+getOrderPath, headers=getOrderHeader).content.decode('utf-8'))

resultString = ''
resultTime = ''
resultTimeFlag = True

if json.loads(orderJson['Message']):
    for orders in json.loads(orderJson['Message']):
        resultString = resultString + 'Order Number: ' + str(orders['orderNumber']) + '<br>'
        if resultTimeFlag == True:
            resultTime = orders['placementDate']
            resultTimeFlag = False
        for items in orders['items']:
            resultString = resultString + str(items['name']) + ': ' + str(items['quantity']) + ' ' + \
                str(items['container']['name']) + '<br>'

