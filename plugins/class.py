from pyrogram import __version__
from bot import Bot  # Assuming Bot is imported from some module
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def aditya_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "aditya":
        await query.message.edit_text(
            text = f" Developed By - Ordinators of [JEE STUDY ROOM Org.](https://t.me/Jeestudyroom)",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

@Bot.on_callback_query()
async def radiux_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "radiux":
        await query.message.edit_text(
            text = f" experiment",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
