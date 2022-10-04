from pyrogram import filters , Client
import time, os
from aiohttp import ClientSession
from Python_ARQ import ARQ
from telegraph import Telegraph
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from telethon import TelegramClient
import logging

StartTime = time.time()

# enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('logs.txt'),
              logging.StreamHandler()],
    level=logging.INFO)

LOGGER = logging.getLogger(__name__)

from nandhabot.config import *

#edit yourself nksama/config.py
OWNER_ID = OWNER_ID
LOG_GROUP_ID = LOG_GROUP_ID
BOT_USERNAME = BOT_USERNAME
SUPPORT_CHAT = SUPPORT_CHAT
UPDATES_CHANNEL = UPDATES_CHANNEL
ARQ_API_KEY = ARQ_API_KEY
ARQ_API_URL = ARQ_API_URL
BOT_ID = BOT_ID
CMD = "~"
TEMP_DOWNLOAD_DIRECTORY = "./" 

###Mogondb Functions # You can use pymongo module also

DB_URL = ""

mongo = MongoClient(DB_URL)
mongodb = mongo.bot 

#main vars set your deploying app
API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
WEBHOOK = bool(os.environ.get('WEBHOOK', False))

async def load_sudoers():
    global SUDOERS
    print("[INFO]: LOADING SUDOERS")
    sudoersdb = mongodb.sudoers
    sudoers = await sudoersdb.find_one({"sudo": "sudo"})
    sudoers = [] if not sudoers else sudoers["sudoers"]
    for user_id in SUDOERS:
        if user_id not in sudoers:
            sudoers.append(user_id)
            await sudoersdb.update_one(
                {"sudo": "sudo"},
                {"$set": {"sudoers": sudoers}},
                upsert=True,
            )

    SUDOERS = (SUDOERS + sudoers) if sudoers else SUDOERS
    print("[INFO]: LOADED SUDOERS")

print("""
┏━┓╋┏┓╋╋╋╋╋╋╋┏┳┓╋╋╋╋┏━━┓╋╋╋┏┓
┃┃┗┓┃┃╋╋╋╋╋╋╋┃┃┃╋╋╋╋┃┏┓┃╋╋┏┛┗┓
┃┏┓┗┛┣━━┳━┓┏━┛┃┗━┳━━┫┗┛┗┳━┻┓┏╋━━┓
┃┃┗┓┃┃┏┓┃┏┓┫┏┓┃┏┓┃┏┓┃┏━┓┃┏┓┃┃┃━━┫
┃┃╋┃┃┃┏┓┃┃┃┃┗┛┃┃┃┃┏┓┃┗━┛┃┗┛┃┗╋━━┃
┗┛╋┗━┻┛┗┻┛┗┻━━┻┛┗┻┛┗┻━━━┻━━┻━┻━━┛
by @NandhaBots - @NandhaxD
""")
bot = Client("nandhabot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="{}/plugins".format(__name__)))
tbot = TelegramClient("Vegeta", API_ID, API_HASH)


aiohttpsession = ClientSession()
arq = ARQ(ARQ_API_URL, ARQ_API_KEY, aiohttpsession)
telegraph = Telegraph()
telegraph.create_account(short_name=BOT_USERNAME)


dev_user = [1491497760, 2083167999]
