#!/usr/bin/env python

import asyncio
import json
from websockets.server import serve

class server:
    async def echo(self, websocket):
        async for message in websocket:
            await websocket.send("server: " + message)

    async def main(self):
        async with serve(self.echo, "localhost", self.port):
            await asyncio.Future()  # run forever
    
    def __init__(self, port):
        self.port = port  
        self.data = {} 
        asyncio.run(self.main())

if __name__ == '__main__':
    initServer = server(8765)
    