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
   Serious Question :
   Aman Aditya ka beta hokar bhi gendu kyu hai ??
    """

    # Inline button that links to your channel
    reply_markup = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Visit Channel 📢", url="https://t.me/jeestudyroom")],
        ]
    )

    # Sending the help message along with the inline button to the user
    await message.reply_text(
        text=help_text,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        quote=True
    )

if __name__ == "__main__":
    print("Bot is running...")
    app.run()  # Run the bot
