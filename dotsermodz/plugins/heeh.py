from pyrogram import Client, filters
from dotsermodz import app


@app.on_message(filters.command("start"))
async def start(client, message):
  await message.reply_text(
        f"Hello, {message.from_user.first_name}!\n\n"
        "Am started 😊\n\n"
        
    )

