# Version: 1.0 Beta
# ©️ 2025 DOTSERMODZ ALL RIGHTS RESERVED
from dotsermodz import app, SUDO ,BOT_NAME
from pyrogram import filters
import os
import sys
import logging
from dotsermodz import app 
from subprocess import getoutput as run
import os
import io

# Configure logging
logging.basicConfig(level=logging.INFO)

# Define the command for rebooting the bot
@app.on_message(filters.command("reboot") & filters.user(SUDO))
async def reboot_bot(client, message):
    await message.reply_text(f"**❍⊷══〘{BOT_NAME}〙═══⊷❍**\n Rebooting the bot...")
    os.execl(sys.executable, sys.executable, *sys.argv)
    logging.info("Bot is restarting...")

# Define the command for shutting down the bot
@app.on_message(filters.command("shutdown")& filters.user(SUDO))
async def shutdown_bot(client, message):
  await message.reply_text(f"**❍⊷══〘{BOT_NAME}〙═══⊷❍**\n Shutting down...")
  await app.stop()
  logging.info("Bot is shutting down...")
  
@app.on_message(filters.command(["cmd", "shell"]) & filters.user(SUDO))
async def shell(client, message):    
    if len(message.command) < 2:
        await message.reply("Give an input!")
        return
    code = message.text.split(None, 1)[1]
    message_text = await message.reply_text("Running")
    output = run(code)
    if len(output) > 4096:
        with io.BytesIO(str.encode(output)) as out_file:
            out_file.name = "shell.txt"
            await message.reply_document(
                document=out_file, disable_notification=True
            )
            await message_text.delete()
    else:
        await message_text.edit(f"**{BOT_NAME} **\nOutput: ```\n\n{output}```")