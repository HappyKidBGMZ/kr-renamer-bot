from bot.utils import not_subscribed
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant


@Client.on_message(filters.private & filters.create(not_subscribed))
async def is_not_subscribed(client, message):
    await message.reply_text(
       text="**β οΈSorry bro,You didn't Joined Our Updates Channel Join now and start againπ**",
       reply_markup=InlineKeyboardMarkup([
           [ InlineKeyboardButton(text="π’πΉπππ πΌπ’ ππππππ π²πππππππ’", url=client.invitelink)]
           ])
       )
