from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot.client import Client
from pyrogram import filters
from pyrogram import types
from bot.core.db.add import add_user_to_database


@Client.on_message(filters.command(["start", "ping"]) & filters.private & ~filters.edited)
async def ping_handler(c: Client, m: "types.Message"):
    await add_user_to_database(c, m)
    await m.reply_photo(
       photo="https://telegra.ph//file/69b6154eaecdaf3845d9f.jpg",
       caption=f"""π Hai {m.from_user.mention} \nπΈ'π π° ππππππ π΅πππ ππππππ+π΅πππ ππ πππππ π²πππππππ π±πΎπ ππππ πΏππππππππ πππππππππ πππππππ! \nπ±πΎπ π²ππππππ π±π’: <a href=https://t.me/beta_bot_updates>Ξ²Ξ£TΞ Ξ²Ξ©TZ</a> \n π€©""",
       reply_markup=InlineKeyboardMarkup( [[
          InlineKeyboardButton("βοΈ OWNER βοΈ", url='https://t.me/JP_Jeol_org')
          ],[
          InlineKeyboardButton('π€ UPDATES', url='https://t.me/beta_bot_updates'),
          InlineKeyboardButton('π₯ SUPPORT', url='https://t.me/BETA_BOTSUPPORT')
          ],[
          InlineKeyboardButton('βοΈ SETTING', callback_data='showSettings')
          ]]
          )
       )
    


@Client.on_message(filters.command("help") & filters.private & ~filters.edited)
async def help_handler(c: Client, m: "types.Message"):
    if not m.from_user:
        return await m.reply_text("I don't know about you sar :(")
    await add_user_to_database(c, m)
    await c.send_flooded_message(
        chat_id=m.chat.id,
        text="I can rename media without downloading it!\n"
             "Speed depends on your media DC.\n\n"
             "Just send me media and reply to it with /rename command.\n\n"
             "To set custom thumbnail reply to any image with /set_thumbnail\n\n"
             "To see custom thumbnail press /show_thumbnail",
        reply_markup=types.InlineKeyboardMarkup([[
           types.InlineKeyboardButton("Show Settings",
                                      callback_data="showSettings")]])
    )
