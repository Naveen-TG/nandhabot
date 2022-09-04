from pyrogram import filters
from pyrogram.types import *
from nandhabot.utils.progress import progress_for_pyrogram
from nandhabot import bot

DOWNLOAD_START = "<b>Downloading To My server !! Pls Wait</b>"
UPLOAD_START = "<b>Downloading Completed Now I'm Uploading Into TeleGram</b>"
AFTER_SUCCESSFUL_UPLOAD_MSG = "<b>Thank you for Using Me Support Our Channel @NandhaBots</b>"

@bot.on_message(filters.command("rename"))
async def rename(_, message):
          try:
             if not message.reply_to_message and not message.reply_to_message.media:
                     return await message.reply("reply to media's")
             elif len(message.command) <2:
                  return await message.reply("provide some text with in extinction!\n for example: `/rename movies.mkv`")
             name = message.text.split(None, 1)[1]
             if message.reply_to_message.media:
                 a = await bot.send_message(
        chat_id=message.chat.id,
        text=DOWNLOAD_START,
        reply_to_message_id=message.id
        )
                 downloads = await message.reply_to_message.download(
                     file_name=name,
                     progress=progress_for_pyrogram,
                     progress_args=(
                DOWNLOAD_START,
                a,
                c_time
            ))
                 await bot.edit_message_text(
                text=UPLOAD_START,
                chat_id=message.chat.id,
                message_id=a.id
                )
                 await message.reply_document(downloads)
                 await bot.edit_message_text(
                text=AFTER_SUCCESSFUL_UPLOAD_MSG,
                chat_id=message.chat.id,
                message_id=a.id,
                disable_web_page_preview=True
           )
                 
          except Exception as error:
                 await message.reply(f"**ERROR**: {error}")
             
