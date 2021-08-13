from Data import Data
from pyrogram import Client, filters


# About Message
@Client.on_message(filters.private & filters.incoming & filters.command("about"))
async def about(bot, msg):
    await bot.send_message(msg.chat.id, Data.ABOUT)
