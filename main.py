# (c) @PredatorHackerzZ

import asyncio
from pyrogram import Client as Bot
from pyrogram import filters
from pyrogram.errors import QueryIdInvalid, FloodWait
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, InlineQuery, CallbackQuery, InlineQueryResultArticle, \
    InputTextMessageContent
from MultiSearchBot.callback import *
from configs import Config

Bot = Client(session_name=Config.SESSION_NAME, api_id=Config.API_ID, api_hash=Config.API_HASH, bot_token=Config.BOT_TOKEN)

Bot.run()
