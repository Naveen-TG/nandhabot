from nandhabot import bot, arq
import logging 
import random
import nandhabot.plugins
from nandhabot.config import SUPPORT_CHAT
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# enable logging



if __name__ == "__main__":
   bot.run()
   with bot:
        bot.send_message(f"@{SUPPORT_CHAT}", "Hello there I'm Now online")
