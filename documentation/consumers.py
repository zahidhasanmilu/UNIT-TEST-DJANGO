from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio
import json

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("websocket connected...")
        self.send({
            "type": "websocket.accept"
        })
        
    def websocket_receive(self, event):
        print("websocket received...")
        print("Message is :", event['text'])
        
        for i in range(5):
            self.send({
                "type": "websocket.send",
                "text": json.dumps({"count":i}),
            })
            sleep(1)
        
            
    def websocket_disconnect(self, event):
        print("websocket disconnected...")
        raise StopConsumer()

class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("websocket connected...")
        await self.send({
            "type": "websocket.accept"
        })
        
    async def websocket_receive(self, event):
        print("websocket received...")
        print("Message is :", event['text'])
        
        for i in range(5):
            await self.send({
                "type": "websocket.send",
                "text": json.dumps({"count":i}),
            })
            await asyncio.sleep(1)        
    
    async def websocket_disconnect(self, event):
        print("websocket disconnected...")
        raise StopConsumer()