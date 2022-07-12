# (c) @PredatorHackerzZ

import asyncio
from pyrogram import Client, filters
from pyrogram.errors import QueryIdInvalid, FloodWait
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, InlineQuery, CallbackQuery, InlineQueryResultArticle, \
    InputTextMessageContent
from MultiSearchBot.scripts import Script
from MultiSearchBot.callback import *
from configs import Config
from tool import SearchYTS, SearchAnime, Search1337x, SearchPirateBay, SearchPyPi

Bot = Client(session_name=Config.SESSION_NAME, api_id=Config.API_ID, api_hash=Config.API_HASH, bot_token=Config.BOT_TOKEN)

@Bot.on_message(filters.command("start"))
async def start_handler(_, message: Message):
    try:
        await message.reply_text(
            text=Script.START_TEXT.format(message.from_user.mention),
            disable_web_page_preview=True,
            parse_mode="html",
            reply_markup=Script.START_BUTTONS
        )
    except FloodWait as e:
        print(f"[{Config.SESSION_NAME}] - Sleeping for {e.x}s")
        await asyncio.sleep(e.x)
        await start_handler(_, message)

Bot.run()
