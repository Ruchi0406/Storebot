import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot import Bot as app
from helper_func import subscribed
from database.database import add_user


# Handler for the /help command
@app.on_message(filters.command('help') & filters.private & subscribed)
async def help_command(client: Client, message):
    # Customizable help message
    help_text = """
    Use command /lectures to get lectures menu...

    bot is under development tab tak @iconic_robot use kro
    nahi to gend marwao...
    """

    # Inline button that links to your channel
    reply_markup = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Visit Channel 📢", url="https://t.me/yourchannelusername")],
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
