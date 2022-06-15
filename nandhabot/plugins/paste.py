from requests import post, get
from nandhabot import bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


def paste(text):
    url = "https://spaceb.in/api/v1/documents/"
    res = post(url, data={"content": text, "extension": "txt"})
    return f"https://spaceb.in/{res.json()['payload']['id']}"


@bot.on_message(filters.command('paste'))
def paste(_, message: Message):
    text = message.reply_to_message
    if text:
        x = paste(text.text)
        message.reply_photo(photo=x, caption=x,
                      reply_markup=InlineKeyboardMarkup(
                          [[InlineKeyboardButton("Paste Link🔗 ", url=x)]]))

    else:
        message.reply_text("Reply to a message!")
