from pyrogram import Client, filters
from pyrogram.types import (
    CallbackQuery,
    InputMediaVideo,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

@app.on_callback_query(filters.regex("aboutw"))
async def gib_repo(client, CallbackQuery: CallbackQuery):
    await CallbackQuery.edit_message_media(
        InputMediaVideo(
            "https://envs.sh/RYX.mp4",
            caption=(
                f"<blockquote>**❖ ๏ ʟᴇᴛ's ɪɴᴛʀᴏᴅᴜᴄᴇ ʀɪsʜᴜ-ᴍᴜsɪᴄ ʙᴏᴛ</blockquote>\n\n"
                f"➻ [ʀɪsʜᴜ-ᴍᴜsɪᴄ](https://t.me/{app.username}) ɪs ᴏɴᴇ ᴏғ ᴛʜᴇ ʙᴇsᴛ ᴍᴜsɪᴄ | ᴠɪᴅᴇᴏ sᴛʀᴇᴀᴍɪɴɢ ʙᴏᴛ ᴏɴ ᴛᴇʟᴇɢʀᴧᴍ ғᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘs ᴀɴᴅ ᴄʜᴧɴɴᴇʟ\n\n"
                f"๏ ᴡʜʏ [˹ ʀɪsʜᴜ ᴍᴜsɪᴄ ˼](https://t.me/UR_RISHU_143) ɪs ʙᴇsᴛ ?\n\n"
                f"⦿━━━━━━━━━━━━━━━━━━━━━⦿\n"
                f"➻ ʙᴇsᴛ sᴏᴜɴᴅ ǫᴜᴀʟɪᴛʏ\n"
                f"➻ ᴍᴜsɪᴄ ʙᴏᴛ ғᴇᴀᴛᴜʀᴇs\n"
                f"➻ ɴᴏ ʏᴛ ɪᴘ ʙʟᴏᴄᴋ ɪssᴜᴇ\n"
                f"➻ ɴᴏ ᴘꝛᴏᴍᴏᴛɪᴏɴᴧʟ ᴧᴅs \n"
                f"➻ ꝛᴇ-ᴇᴅɪᴛᴇᴅ ᴄᴏʀᴇ | ʜɪɢʜʟʏ ᴏᴘᴛɪᴍɪsᴇ\n"
                f"➻ ɴᴏ ʟᴧɢ ᴀɴᴅ ᴅᴏᴡɴ-ᴛɪᴍᴇ\n"
                f"➻ ᴍᴀɴʏ ᴍᴏʀᴇ ғᴇᴀᴛᴜʀᴇs........\n"
                f"⦿━━━━━━━━━━━━━━━━━━━━━⦿\n\n"
                f"ᴀʟʟ ᴛʜᴇ ғᴇᴀᴛᴜʀᴇs ᴀʀᴇ ᴡᴏʀᴋɪɴɢ ғɪɴᴇ\n\n"
                f"❖ [Jᴏɪɴ ᴄʜᴀɴɴᴇʟ](https://t.me/UR_RISHU_143) |×| [ɢʀᴏᴜᴘ](https://t.me/UR_support07)**"
            ),
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="❖ ᴛᴧᴘ тᴏ sᴇᴇ ᴍᴧɢɪᴄ ❖",
                        url=f"https://t.me/{app.username}?startgroup=true",
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="• ʙᴧsɪᴄ ɢᴜɪᴅᴇ •", callback_data="basict"
                    ),
                    InlineKeyboardButton(
                        text="• ᴅᴏɴᴀᴛᴇ •", callback_data="doniiyyf"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text="• sᴜʙsᴄʀɪʙᴇ •", callback_data="subplanh"
                    ),
                    InlineKeyboardButton(
                        text="• sᴜᴘᴘᴏʀᴛ •", callback_data="suppo"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text="⌬ ʙᴀᴄᴋ ⌬", callback_data="settingsback_helper"
                    )
                ],
            ]
        ),
    )