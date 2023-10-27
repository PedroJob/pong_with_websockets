#!/usr/bin/env python
from pynput.keyboard import Listener
import asyncio
from websockets.sync.client import connect
import json

class client: 
    def __init__(self, name, port):
        self.server = connect(f"ws://localhost:{port}")
        self.name = name
    """
    def onPress(self, key):
        data = {}
        data['player'] = self.name
        if(key == 'Key.up'):
            data['movement'] = 1
            self.sendMessage(json.dumps(data))
        
        if(key == 'Key.down'):
            data['movement'] = 0
            self.sendMessage(0)
    
    def onRelease(self, key):
        pass
    
    def keyListen(self):
        with Listener(on_press= self.onPress, on_release= self.onRelease) as listener:
            listener.join()
    """
    def sendMessage(self, message):
        self.server.send(message)
        echo = self.server.recv()
        print(f"Received: {echo}")
        
if __name__ == "__main__":
    initClient = client('job', 8765)
    while True: 
        message = input("digite a msng: ")
        initClient.sendMessage(message=message)
