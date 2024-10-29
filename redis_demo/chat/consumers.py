# chat/consumers.py

import asyncio

import aioredis
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Set up Redis connection and subscribe to the "chat" channel
        self.redis = aioredis.from_url("redis://redis:6379")
        self.pubsub = self.redis.pubsub()
        await self.pubsub.subscribe("chat")

        # Accept the WebSocket connection
        await self.accept()

        # Start listening for messages in Redis pub/sub channel
        await self.channel_layer.group_add("chat_group", self.channel_name)
        # Use asyncio.create_task to start listening for messages
        self.listen_task = asyncio.create_task(self.listen_for_messages())

    async def disconnect(self, close_code):
        await self.pubsub.unsubscribe("chat")
        await self.redis.close()
        await self.channel_layer.group_discard("chat_group", self.channel_name)

        # Optionally cancel the listen task if it's still running
        if self.listen_task:
            self.listen_task.cancel()

    async def listen_for_messages(self):
        async for message in self.pubsub.listen():
            if message["type"] == "message":
                event_data = message["data"].decode("utf-8")
                await self.send(text_data=event_data)

    async def receive(self, text_data):
        # Publish incoming message to the Redis "chat" channel
        await self.redis.publish("chat", text_data)
