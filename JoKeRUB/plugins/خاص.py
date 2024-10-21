import asyncio
from telethon.tl.types import Message
from JoKeRUB import l313l
from JoKeRUB.core.logger import logging
from telethon.errors.rpcerrorlist import MessageNotModifiedError
from ..Config import Config
from ..core.managers import edit_delete
from ..helpers.tools import media_type
from ..helpers.utils import _format
from ..sql_helper import no_log_pms_sql
from ..sql_helper.globals import addgvar, gvarstatus
from . import BOTLOG, BOTLOG_CHATID

@l313l.ar_cmd(
    pattern="خاص(?:\s|$)([\s\S]*)",
    command=("خاص", plugin_category),
    info={
        "header": "To log the replied message to bot log group so you can check later.",
        "الاسـتخـدام": [
            "{tr}خاص",
        ],
    },
)
async def log(log_text):
    "To log the replied message to bot log group"
    if BOTLOG:
        if log_text.reply_to_msg_id:
            reply_msg = await log_text.get_reply_message()
            await reply_msg.forward_to("me")
        elif log_text.pattern_match.group(1):
            user = f"#التخــزين / ايـدي الدردشــه : {log_text.chat_id}\n\n"
            textx = user + log_text.pattern_match.group(1)
            await log_text.client.send_message(me, textx)
        else:
            await log_text.edit("**⌔┊بالــرد على اي رسـاله لحفظهـا في كـروب التخــزين**")
            return
        await log_text.edit("**⌔┊تـم الحفـظ في كـروب التخـزين .. بنجـاح ✓**")
    else:
        await log_text.edit("**⌔┊عـذراً .. هـذا الامـر يتطلـب تفعيـل فـار التخـزين اولاً**")
    await asyncio.sleep(2)
    await log_text.delete()

