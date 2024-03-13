from pyrogram import __version__
from bot import Bot
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def callback_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "aditya":
        await aditya_handler(client, query)
    elif data == "radiux":
        await radiux_handler(client, query)

async def aditya_handler(client: Bot, query: CallbackQuery):
    await query.message.edit_text(
        text = f"gendu",
        disable_web_page_preview = True,
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🔒 Close", callback_data = "close")
                ]
            ]
        )
    )

async def radiux_handler(client: Bot, query: CallbackQuery):
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

@Bot.on_callback_query()
async def close_handler(client: Bot, query: CallbackQuery):
    if query.data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
