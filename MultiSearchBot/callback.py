#callback_data
#!/usr/bin/env python3
# (c) @PredatorHackerzZ

from pyrogram import Client 
from MultiSearchBot.scripts import Script
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery



@Bot.on_callback_query()
async def button(_, message: Message):
    if update.data == "home":
        await message.edit_text(
            text=Script.START_TEXT.format(update.from_user.mention),
            reply_markup=Script.START_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "help":
        await message.edit_text(
            text=Script.HELP_TEXT,
            reply_markup=Script.HELP_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "about":
        await message.edit_text(
            text=Script.ABOUT_TEXT,
            reply_markup=Script.ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "inline_buttons":
        await message.edit_text(
            text=Script.INLINE_TEXT,
            reply_markup=Script.SEARCH_BUTTONS,
            disable_web_page_preview=True
        )

    else:
        await message.delete()
