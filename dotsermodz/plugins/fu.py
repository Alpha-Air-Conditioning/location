import base64
import os
import datetime
from pymongo import MongoClient
from pyrogram import Client, filters
from pyrogram.types import Message

# Your existing app instance and sudo list
from dotsermodz import app, SUDO , MONGO_URI

DB_NAME = "peer_database"
COLLECTION_NAME = "peers"

mongo_client = MongoClient(MONGO_URI)
db = mongo_client[DB_NAME]
peer_collection = db[COLLECTION_NAME]

# /gen command
@app.on_message(filters.command("gen") & filters.user(SUDO))
async def generate_secret_code(client: Client, message: Message):
    if len(message.command) < 3:
        await message.reply("Usage: /gen peer_id expiry: 1m|lifetime")
        return

    peer_id = message.command[1]
    expiry_option = message.command[2].lower()

    if expiry_option == "1m":
        expiry_date = datetime.datetime.utcnow() + datetime.timedelta(days=30)
    elif expiry_option == "lifetime":
        expiry_date = None
    else:
        await message.reply("Invalid expiry option. Use '1m' or 'lifetime'.")
        return

    secret_code = base64.b64encode(f"{peer_id}_secret".encode()).decode()
    peer_name = message.from_user.first_name if message.from_user else "Unknown"

    peer_data = {
        "peer_id": peer_id,
        "name": peer_name,
        "secret": secret_code,
        "expiry": expiry_date
    }

    peer_collection.update_one({"peer_id": peer_id}, {"$set": peer_data}, upsert=True)

    expiry_text = "Lifetime" if expiry_date is None else f"Expires on {expiry_date.strftime('%Y-%m-%d')}"
    await message.reply(
        f"Generated secret code for Peer ID {peer_id}:\n{secret_code}\n{expiry_text}"
    )

# /remove command
@app.on_message(filters.command("remove") & filters.user(SUDO))
async def remove_peer_data(client: Client, message: Message):
    if len(message.command) < 2:
        await message.reply("Usage: /remove <peer_id>")
        return

    peer_id = message.command[1]
    result = peer_collection.delete_one({"peer_id": peer_id})

    if result.deleted_count > 0:
        await message.reply(f"Removed data for Peer ID {peer_id}.")
    else:
        await message.reply(f"No data found for Peer ID {peer_id}.")

# /viewall command
@app.on_message(filters.command("viewall") & filters.user(SUDO))
async def view_all_peers(client: Client, message: Message):
    peers = list(peer_collection.find())
    if not peers:
        await message.reply("No data available.")
        return

    reply_text = "Stored Peer Data:\n\n"
    for peer in peers:
        expiry = peer.get("expiry")
        if expiry:
            if not isinstance(expiry, datetime.datetime):
                expiry = datetime.datetime.strptime(expiry, "%Y-%m-%dT%H:%M:%S.%f")
            days_left = (expiry - datetime.datetime.utcnow()).days
            expiry_text = f"{days_left} days left" if days_left > 0 else "Expired"
        else:
            expiry_text = "Lifetime"

        reply_text += (
            f"Peer ID: {peer['peer_id']}\n"
            f"Name: {peer['name']}\n"
            f"Secret: {peer['secret']}\n"
            f"Expiry: {expiry_text}\n\n"
        )

    await message.reply(reply_text)
