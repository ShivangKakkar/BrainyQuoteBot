from Data import Data
from pyrogram import Client, filters


# Help Message
@Client.on_message(filters.private & filters.incoming & filters.command("help"))
async def _help(bot, msg):
    await bot.send_message(
        msg.chat.id,
        "**Here's how to use me **\n" + Data.HELP
    )
