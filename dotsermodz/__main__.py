# Version: 1.0 Beta
# ©️ 2025 DOTSERMODZ ALL RIGHTS RESERVED
from dotsermodz.keep import web 
from dotsermodz import app
from dotsermodz.lib.Base import strt_msgs , crymore
from pyrogram import idle
import logging
import asyncio


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - ☠➥%(message)s')

async def main():
     await app.start() 
     await crymore()
     web.keep_alive()
     await idle() 


if __name__ == "__main__":
    print(strt_msgs)  
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
