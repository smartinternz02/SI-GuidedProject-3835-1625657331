import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "qqjb5y",
        "typeId": "Device_1",
        "deviceId":"1223"
    },
    "auth": {
        "token": "12090009"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    temp=random.randint(0,100)
    hum=random.randint(0,100)
    myData={'waterlevel':temp, 'intensity':hum}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
