import wiotp.sdk.device
import time
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
    print("Username Recieved from the APP: ",cmd.data['Username'])
    print("Password Recieved from the APP: " ,cmd.data['Password'])
    
try:
    client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
    client.connect()
    while True:
        client.commandCallback = myCommandCallback
        time.sleep(2)
except KeyboardInterrupt:
    client.disconnect()
 