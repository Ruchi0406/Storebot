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
    help_text = """🆘 **Help & Commands Guide**

Here you can customize the help message to provide information about how to use your bot or list the available commands.

- `/start`: Start the bot and get the welcome message.
- `/help`: Get this help message.

Feel free to customize this message according to your bot's functionality."""

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
