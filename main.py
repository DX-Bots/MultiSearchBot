#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @PredatorHackerzZ | @TeamTeleRoid

# the logging things
import logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

from pyrogram import Client, filters

from configs import Config

Bot = Client(
    session_name=Config.SESSION_NAME,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

Bot.run()
