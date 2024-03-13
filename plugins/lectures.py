import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot import Bot as aditya
from helper_func import subscribed
from database.database import add_user

# Handler for the /help command
@aditya.on_message(filters.command('lectures') & filters.private & subscribed)
async def help_command(client: Client, message):
    # Customizable help message
    help_text = """
  Select your class --
    """

    # Inline button that links to your channel
    reply_markup = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Visit Channel 📢", url="https://t.me/jeestudyroom")],
            [InlineKeyboardButton("class 11", callback_data="aditya"),
             InlineKeyboardButton("class 12", callback_data="radiux")
            ],
        ]
    )

    # Sending the help message along with the inline button to the user
    await message.reply_text(
        text=help_text,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        quote=True
    )

# Decorate the functions with Bot event handler decorators
@aditya.on_callback_query()
async def aditya_handler(client: Client, query):
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

@aditya.on_callback_query()
async def radiux_handler(client: Client, query):
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

# Start the client
async def main():
    await aditya.start()
    print("Bot is running...")
    await aditya.idle()

if __name__ == "__main__":
    asyncio.run(main())
