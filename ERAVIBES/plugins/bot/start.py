import time
import random 
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.__future__ import VideosSearch

import config
from ERAVIBES import app
from ERAVIBES.misc import _boot_
from ERAVIBES.plugins.sudo.sudoers import sudoers_list
from ERAVIBES.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
    is_on_off,
)
from ERAVIBES.utils.decorators.language import LanguageStart
from ERAVIBES.utils.formatters import get_readable_time
from ERAVIBES.utils.inline import help_pannel, private_panel, start_panel
from config import BANNED_USERS
from strings import get_string

IMAGE = [
"https://envs.sh/kJw.jpg",
"https://envs.sh/kSk.jpg",
"https://envs.sh/kJB.jpg",
"https://envs.sh/kJW.jpg",
"https://envs.sh/kJ0.jpg",
]

# Updated list with emojis
D = ["😘", "👾", "🤝", "👀", "❤️‍🔥", "💘", "😍", "😇", "🕊️", "🐳", "🎉", "🏆", "🗿", "⚡", "💯", "👌", "🍾"]

#aboutt

@app.on_callback_query(filters.regex("gibt_source") & ~BANNED_USERS)
@languageCB
async def gib_repo(client, CallbackQuery, _):
    await CallbackQuery.edit_message_media(
        InputMediaPhoto(
            "https://envs.sh/kJW.jpg",  # Replace with the URL of your photo
            caption= f"<blockquote>**❖ ๏ ʟᴇᴛ's ɪɴᴛʀᴏᴅᴜᴄᴇ ʀɪsʜᴜ-ᴍᴜsɪᴄ ʙᴏᴛ</blockquote>\n\n➻ [ʀɪsʜᴜ-ᴍᴜsɪᴄ](https://t.me/{app.username})  ɪs ᴏɴᴇ ᴏғ ᴛʜᴇ ʙᴇsᴛ ᴍᴜsɪᴄ | ᴠɪᴅᴇᴏ sᴛʀᴇᴀᴍɪɴɢ ʙᴏᴛ ᴏɴ ᴛᴇʟᴇɢʀᴧᴍ ғᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘs ᴀɴᴅ ᴄʜᴧɴɴᴇʟ\n\n๏ ᴡʜʏ [˹ ʀɪsʜᴜ ᴍᴜsɪᴄ ˼](https://t.me/UR_RISHU_143) ɪs ʙᴇsᴛ ?\n\n⦿━━━━━━━━━━━━━━━━━━━━━⦿\n➻ ʙᴇsᴛ sᴏᴜɴᴅ ǫᴜᴀʟɪᴛʏ\n➻ ᴍᴜsɪᴄ ʙᴏᴛ ғᴇᴀᴛᴜʀᴇs\n➻ ɴᴏ ʏᴛ ɪᴘ ʙʟᴏᴄᴋ ɪssᴜᴇ\n➻ ɴᴏ ᴘꝛᴏᴍᴏᴛɪᴏɴᴧʟ ᴧᴅs \n➻ ꝛᴇ-ᴇᴅɪᴛᴇᴅ ᴄᴏʀᴇ | ʜɪɢʜʟʏ ᴏᴘᴛɪᴍɪsᴇ\n➻ ɴᴏ ʟᴧɢ ᴀɴᴅ ᴅᴏᴡɴ-ᴛɪᴍᴇ\n➻ ᴍᴀɴʏ ᴍᴏʀᴇ ғᴇᴀᴛᴜʀᴇs........\n⦿━━━━━━━━━━━━━━━━━━━━━⦿\n\nᴀʟʟ ᴛʜᴇ ғᴇᴀᴛᴜʀᴇs ᴀʀᴇ ᴡᴏʀᴋɪɴɢ ғɪɴᴇ\n\n❖ [Jᴏɪɴ ᴄʜᴀɴɴᴇʟ](https://t.me/UR_RISHU_143) |×| [ɢʀᴏᴜᴘ](https://t.me/UR_support07)**"
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(
                    text="❖ ᴛᴧᴘ тᴏ sᴇᴇ ᴍᴧɢɪᴄ ❖",
                    url=f"https://t.me/{app.username}?startgroup=true",
                )],
                [InlineKeyboardButton(text="• ʙᴧsɪᴄ ɢᴜɪᴅᴇ •", callback_data=f"basict"),
                 InlineKeyboardButton(text="• ᴅᴏɴᴀᴛᴇ •", callback_data=f"doniiyyf")],
                [InlineKeyboardButton(text="• sᴜʙsᴄʀɪʙᴇ •", callback_data=f"subplanh"),
                 InlineKeyboardButton(text="• sᴜᴘᴘᴏʀᴛ •", callback_data=f"suppo")],
                [InlineKeyboardButton(text="⌬ ʙᴀᴄᴋ ⌬", callback_data=f"settingsback_helper")],
            ],
        ),
    )



@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    await message.react(random.choice(D))
        
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            keyboard = help_pannel(_)
            return await message.reply_photo(
                random.choice(IMAGE),
                caption=_["help_1"].format(config.SUPPORT_CHAT),
                reply_markup=keyboard,
            )
        if name[0:3] == "sud":
            await sudoers_list(client=client, message=message, _=_)
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"❖ {message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>sᴜᴅᴏʟɪsᴛ</b>.\n\n<b>● ᴜsᴇʀ ɪᴅ ➥</b> <code>{message.from_user.id}</code>\n<b>● ᴜsᴇʀɴᴀᴍᴇ ➥</b> @{message.from_user.username}",
                )
            return
        if name[0:3] == "inf":
            m = await message.reply_text("🔎")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in (await results.next())["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = _["start_6"].format(
                title, duration, views, published, channellink, channel, app.mention
            )
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=_["S_B_8"], url=link),
                        InlineKeyboardButton(text=_["S_B_9"], url=config.SUPPORT_CHAT),
                    ],
                ]
            )
            await m.delete()
            await app.send_photo(
                chat_id=message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                reply_markup=key,
            )
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"❖ {message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>ᴛʀᴀᴄᴋ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</b>.\n\n<b>● ᴜsᴇʀ ɪᴅ ➥</b> <code>{message.from_user.id}</code>\n<b>● ᴜsᴇʀɴᴀᴍᴇ ➥</b> @{message.from_user.username}",
                )
    else:
        out = private_panel(_)
        await message.reply_photo(
            random.choice(IMAGE),
            caption=_["start_2"].format(message.from_user.mention, app.mention),
            reply_markup=InlineKeyboardMarkup(out),
        )
        if await is_on_off(2):
            return await app.send_message(
                chat_id=config.LOGGER_ID,
                text=f"❖ {message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ.\n\n<b>● ᴜsᴇʀ ɪᴅ ➥</b> <code>{message.from_user.id}</code>\n<b>● ᴜsᴇʀɴᴀᴍᴇ ➥</b> @{message.from_user.username}",
            )


@app.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def testbot(client, message: Message, _):
    uptime = int(time.time() - _boot_)
    chat_id = message.chat.id
    try:
        await message.react(random.choice(D))
    except Exception as e:
        pass
        
    await message.reply_text(_["start_1"])

    return await add_served_chat(message.chat.id)


@app.on_message(filters.new_chat_members, group=-1)
async def welcome(client, message: Message):
    chat_id = message.chat.id
    if config.PRIVATE_BOT_MODE == str(True):
        if not await is_served_private_chat(message.chat.id):
            await message.reply_text(
                "This Bot's private mode has been enabled only my owner can use this if want to use in your chat so say my Owner to authorize your chat."
            )
            return await app.leave_chat(message.chat.id)
    else:
        await add_served_chat(chat_id)
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
            if member.id == app.id:
                chat_type = message.chat.type
                if chat_type != ChatType.SUPERGROUP:
                    await message.reply_text(_["start_5"])
                    return await app.leave_chat(message.chat.id)
                if chat_id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_6"].format(
                            f"https://t.me/{app.username}?start=sudolist"
                        )
                    )
                    return await app.leave_chat(chat_id)
                userbot = await get_assistant(message.chat.id)
                out = start_pannel(_)
                await message.reply_text(
                    _["start_2"].format(
                        app.mention,
                        userbot.username,
                        userbot.id,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
            if member.id in config.OWNER_ID:
                return await message.reply_text(
                    _["start_3"].format(app.mention, member.mention)
                )
            if member.id in SUDOERS:
                return await message.reply_text(
                    _["start_4"].format(app.mention, member.mention)
                )
            return
        except Exception:

            return
