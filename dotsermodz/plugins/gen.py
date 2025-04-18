import base64
from pymongo import MongoClient
from pyrogram import Client, filters
from pyrogram.types import Message
from dotsermodz import app
from dotenv import load_dotenv
import os
load_dotenv()
# MongoDB Configuration
DB_NAME = "peer_database"
COLLECTION_NAME = "peers"
MONGO_URI = os.getenv("MONGO_URI","")
# Initialize MongoDB client
mongo_client = MongoClient(MONGO_URI)
db = mongo_client[DB_NAME]
peer_collection = db[COLLECTION_NAME]


@app.on_message(filters.command("gen"))
async def generate_secret_code(client: Client, message: Message):
    if len(message.command) < 2:
        await message.reply("Usage: /gen <peer_id>")
        return

    peer_id = message.command[1]

    # Generate a base64 secret code
    secret_code = base64.b64encode(f"{peer_id}_secret".encode()).decode()

    # Get peer name
    peer_name = message.from_user.first_name if message.from_user else "Unknown"

    # Save the peer data in MongoDB
    peer_data = {
        "peer_id": peer_id,
        "name": peer_name,
        "secret": secret_code
    }
    peer_collection.update_one({"peer_id": peer_id}, {"$set": peer_data}, upsert=True)

    await message.reply(f"Generated secret code for Peer ID {peer_id}:\n{secret_code}")

@app.on_message(filters.command("rm"))
async def remove_peer_data(client: Client, message: Message):
    if len(message.command) < 2:
        await message.reply("Usage: /remove <peer_id>")
        return

    peer_id = message.command[1]

    # Remove the peer data from MongoDB
    result = peer_collection.delete_one({"peer_id": peer_id})

    if result.deleted_count > 0:
        await message.reply(f"Removed data for Peer ID {peer_id}.")
    else:
        await message.reply(f"No data found for Peer ID {peer_id}.")



@app.on_message(filters.command("viewall"))
async def view_all_peers(client: Client, message: Message):
    # Fetch all peer data from MongoDB
    peers = peer_collection.find()  # This returns a Cursor object

    # Check if there are any documents
    if not peer_collection.count_documents({}):  # Remove 'await' here
        await message.reply("No data available.")
        return

    reply_text = "Stored Peer Data:\n\n"
    for peer in peers:  # Use a synchronous for loop
        reply_text += f"Peer ID: {peer['peer_id']}\nName: {peer['name']}\nSecret: {peer['secret']}\n\n"

    await message.reply(reply_text)
