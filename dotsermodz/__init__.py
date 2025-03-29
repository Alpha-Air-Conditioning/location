# Version: 1.0 Beta
# ©️ 2021 DOTSERMODZ ALL RIGHTS RESERVED
from pyrogram import Client
from dotenv import load_dotenv
import os
import time

load_dotenv()

# Retrieve environment variables with safe defaults
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
BOT_TOKEN = os.getenv('BOT_TOKEN')
SUDO = list(map(int, os.getenv("SUDO", "0").split(',')))
PORT = int(os.getenv("PORT", 5000))
BOT_NAME = os.getenv("BOT_NAME", "DOTSERMODZ")


app = Client(
    "dotsermodz-basebot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=dict(root="dotsermodz/plugins"), 
)

