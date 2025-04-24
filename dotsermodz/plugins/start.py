from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from dotsermodz import app

# Define the web app URL
WEB_APP_URL = "http://websteamtg-yfqk.onrender.com/"

@app.on_message(filters.command("start"))
async def send_webapp(client, message):
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "Open WebApp", 
                    web_app=WebAppInfo(url=f"{WEB_APP_URL}login?id={message.chat.id}")
                )
            ]
        ]
    )
    await message.reply(
        "Click the button below to open the web app:",
        reply_markup=keyboard,
        protect_content=True
    )
