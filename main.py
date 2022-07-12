#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @PredatorHackerzZ | @TeamTeleRoid

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):

from pyrogram import Client as Bot
from pyrogram import filters
from MultiSearchBot.callback import *
from configs import *

Bot = Client(session_name=Config.SESSION_NAME, api_id=Config.API_ID, api_hash=Config.API_HASH, bot_token=Config.BOT_TOKEN)

Bot.run()
