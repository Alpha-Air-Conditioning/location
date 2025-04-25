from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from dotsermodz import app

# Web app URL
WEB_APP_URL = "https://websteamtg-yfqk.onrender.com/"

async def send_webapp(client, message):
    user_id = message.chat.id
    login_url = f"{WEB_APP_URL}login?id={user_id}"

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Open WebApp",
                    web_app=WebAppInfo(url=login_url)
                )
            ]
        ]
    )

    await message.reply(
        text="Click the button below to open the web app:",
        reply_markup=keyboard,
        protect_content=True
    )

@app.on_message(filters.command("start"))
async def start_command(client, message):
    await send_webapp(client, message)


