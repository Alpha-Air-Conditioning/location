from pyrogram import Client, filters
from dotsermodz import app
SOURCE_CHAT_ID = -1002476441593 #edit
TARGET_CHAT_ID = -1002620317808 # edit
@app.on_message(filters.chat(SOURCE_CHAT_ID))
async def auto_forward(client, message):
    await message.copy(TARGET_CHAT_ID)
