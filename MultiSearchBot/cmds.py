#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @PredatorHackerzZ

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
from MultiSearchBot.callback import *
from configs import Config

# the Strings used for this "thing"
from MultiSearchBot.scripts import Script
from pyrogram import filters
from pyrogram import Client as Bot
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery, ForceReply


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



@Bot.on_message(filters.command("help"))
async def help_handler(_, message: Message):
    try:
        await message.reply_text(
            text=Script.HELP_TEXT.format(message.from_user.mention),
            disable_web_page_preview=True,
            parse_mode="html",
            reply_markup=Script.HELP_BUTTONS
        )
    except FloodWait as e:
        print(f"[{Config.SESSION_NAME}] - Sleeping for {e.x}s")
        await asyncio.sleep(e.x)
        await help_handler(_, message)


@Bot.on_message(filters.command("about"))
async def about_handler(_, message: Message):
    try:
        await message.reply_text(
            text=Script.ABOUT_TEXT.format(message.from_user.mention),
            disable_web_page_preview=True,
            parse_mode="html",
            reply_markup=Script.ABOUT_BUTTONS
        )
    except FloodWait as e:
        print(f"[{Config.SESSION_NAME}] - Sleeping for {e.x}s")
        await asyncio.sleep(e.x)
        await about_handler(_, message)
