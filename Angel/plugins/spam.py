from .. import Raizen
import asyncio
import base64
import os

from telethon import events,functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

Raizen_USER = [1801571739]

@Raizen.on(
    events.NewMessage(pattern="^/spam ?(.*)", func=lambda e: e.sender_id in Raizen_USER)
)
async def spammer(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        counter = int(message[6:8])
        spam_message = str(e.text[8:])
        await asyncio.wait([e.respond(spam_message) for i in range(counter)])
        await e.delete()
