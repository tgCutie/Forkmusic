from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAEBkKdhbF6MOlRpJ1z1AZbap8oVZy_OOAACMAUAAuB8YVcIDB5XRm6wkx4E")
