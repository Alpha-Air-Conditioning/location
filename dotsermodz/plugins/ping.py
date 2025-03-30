# Version: 1.0 Beta
# ©️ 2025 DOTSERMODZ ALL RIGHTS RESERVED
from dotsermodz import app , BOT_NAME
from pyrogram import filters
import logging
import time

# This is a simple ping command that will reply with "pong" and the response time in milliseconds
@app.on_message(filters.command("ping"))
async def ping_command(app, message):
    start_time = time.time()
    await message.reply_text("pong")
    end_time = time.time()
    response_time = int((end_time - start_time) * 1000)
    await message.reply_text(f"**❍⊷══〘{BOT_NAME}〙═══⊷❍**\nResponse time: {response_time} ms")
    logging.info(f"Ping command received and replied with pong in {response_time} ms")