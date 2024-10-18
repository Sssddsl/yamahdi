#all write Codes By Team Aljoker @jepthon
#By Hussein @lMl10l
import asyncio
import random
import re
import json
import base64
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from asyncio.exceptions import TimeoutError
from telethon import events
from ..sql_helper.memes_sql import get_link, add_link, delete_link, BASE, SESSION, AljokerLink
from telethon.errors.rpcerrorlist import YouBlockedUserError
#ياقائم آل محمد
from JoKeRUB import l313l
from ..helpers.utils import reply_id
plugin_category = "tools"

@l313l.on(admin_cmd(pattern="حالتي ?(.*)"))
async def _(event):
    await event.edit("**- يتم التاكد من حالتك اذا كنت محظور او لا**")
    async with bot.conversation("@SpamBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=178220800)
            )
            await conv.send_message("/start")
            response = await response
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("** اولا الغي حظر @SpamBot وحاول مجددا**")
            return
        await event.edit(f"- {response.message.message}\n @jepthon")


@l313l.on(admin_cmd(pattern="الاغنية ?(.*)"))
async def _(event):
    "To reverse search music by bot."
    if not event.reply_to_msg_id:
        return await event.edit("**▾∮ يجب الرد على الاغنيه اولا**")
    reply_message = await event.get_reply_message()
    chat = "@auddbot"
    try:
        async with event.client.conversation(chat) as conv:
            try:
                await event.edit("**▾∮ يتم التعرف على الاغنية انتظر**")
                start_msg = await conv.send_message("/start")
                response = await conv.get_response()
                send_audio = await conv.send_message(reply_message)
                check = await conv.get_response()
                if not check.text.startswith("Audio received"):
                    return await event.edit(
                        "**▾∮ يجب ان يكون حجم الاغنيه من 5 الى 10 ثواني **."
                    )
                await event.edit("- انتظر قليلا")
                result = await conv.get_response()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("```Mohon buka blokir (@auddbot) dan coba lagi```")
                return
            namem = f"**الأغنية : **{result.text.splitlines()[0]}\
        \n\n**التفاصيـل : **{result.text.splitlines()[2]}"
            await event.edit(namem)
            await event.client.delete_messages(
                conv.chat_id,
                [start_msg.id, send_audio.id, check.id, result.id, response.id],
            )
    except TimeoutError:
        return await event.edit("***حدث خطا ما حاول مجددا**")


@l313l.on(admin_cmd(pattern="ايميل وهمي(?: |$)(.*)"))
async def _(event):
    chat = "@TempMailBot"
    geez = await event.edit("**جاري انشاء بريد ...**")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=220112646)
            )
            await conv.send_message("/start")
            await asyncio.sleep(1)
            await conv.send_message("/create")
            response = await response
            l313lmail = (response).reply_markup.rows[2].buttons[0].url
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await geez.edit("**الغي حظر @TempMailBot  و حاول مجددا**")
            return
        await event.edit(
            f"الايميل الخاص هو `{response.message.message}`\n[ اضغط هنا لرؤية من رسائل الايميل الواردة]({l313lmail})"
        )
        @l313l.on(admin_cmd(outgoing=True, pattern="غنيلي$"))
async def aljoker313(joker313):
  rl = random.randint(1,385)
  url = f"https://t.me/DwDi1/{rl}"
  await joker313.client.send_file(joker313.chat_id,url,caption="᯽︙ BY : @jepthon 🎀",parse_mode="html")
  await joker313.delete()
    
@l313l.on(admin_cmd(outgoing=True, pattern="شعر$"))
async def jepvois(vois):
  rl = random.randint(2,101)
  url = f"https://t.me/L1BBBL/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="᯽︙ BY : @jepthon 🎀",parse_mode="html")
  await vois.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="قران$"))
async def jepvois(vois):
  rl = random.randint(2,101)
  url = f"https://t.me/QuraanJep/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="᯽︙ BY : @jepthon 🤲🏻☪️",parse_mode="html")
  await vois.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="ثيم$"))
async def jepThe(theme):
  rl = random.randint(2,510)
  url = f"https://t.me/GSSSD/{rl}"
  await theme.client.send_file(theme.chat_id,url,caption="᯽︙ THEME BY : @jepthon 🎊",parse_mode="html")
  await theme.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="لاتغلط$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/MemeSoundJep/4"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="بجيت$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/MemeSoundJep/5"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="نشاقة$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/MemeSoundJep/3"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="احب الله$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/MemeSoundJep/2"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="ببجي$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/vipabh/1134"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="شنهي$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/vipabh/1115"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="انمي2$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/MemeSoundJep/9"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="انمي3$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/MemeSoundJep/11"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="انمي4$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/MemeSoundJep/12"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="انمي5$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/MemeSoundJep/13"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="انمي6$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/MemeSoundJep/14"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="انمي7$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/MemeSoundJep/15"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="انمي8$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/MemeSoundJep/16"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="انمي9$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/MemeSoundJep/17"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="انمي10$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/MemeSoundJep/18"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="زيج2$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/MemeSoundJep/19"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="زيج$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/MemeSoundJep/20"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="عبود$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/vipabh/1162"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="تف$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/MemeSoundJep/1161"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="احب العراق$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/MemeSoundJep/27"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="مستمرة الكلاوات$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/MemeSoundJep/28"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="حبك$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/MemeSoundJep/29"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="اخت التنيج$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/MemeSoundJep/30"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="اذا اكمشك$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/MemeSoundJep/31"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="اسكت$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/MemeSoundJep/32"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="بوبجي$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/vipabh/1134"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="شش$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/vipabh/79"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="ماذا"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/vipabh/81"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="هه$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/vipabh/338"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="شماته$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/MemeSoundJep/37"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="ماكدر$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/MemeSoundJep/38"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="مرهم$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/VIPABH/537"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="سبحان$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/vipabh/541"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="طط$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/vipabh/568"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="لاا$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/vipabh/571"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="وخر$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/vipabh/589"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="هههه$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/MemeSoundJep/44"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="انجب"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/vipabh/592"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="امريكا$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/vipabh/1113"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="شسوي$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/vipabh/1114"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="ها$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/vipabh/1115"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="لتغلط$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/MemeSoundJep/51"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="مي$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/VIPABH/1116"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="انعل$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/VIPABH/597"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="فلا$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/VIPABH/1160"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="طاح$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/VIPABH/612"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="لب$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/VIPABH/614"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="خوش"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/MemeSoundJep/57"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="صل$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/VIPABH/735"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="ط$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/vipabh/736"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="يامرحبا$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/MemeSoundJep/60"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="فد$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/VIPABH/748"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="ه$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/VIPABH/967"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="كعبة$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/VIPABH/1155"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern= "قران$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/VIPABH/980"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="طبك$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/MemeSoundJep/65"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="دكي$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/VIPABH/987"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="نعال"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/VIPABH/1156"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="خاف حرام$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/MemeSoundJep/68"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="دنجب$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/VIPABH/988"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="روح$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/MemeSoundJep/71"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="مزنجر$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/VIPABH/997"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="الهي$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/vipabh/23"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="ملحد$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/vipabh/1110"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="يدكتور$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/vipabh/1107"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="اي$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/vipabh/1098"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="الماوارثها$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/vipabh/1093"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="يولن$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/vipabh/292"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="نيو$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/vipabh/5"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="نوكيا$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/vipabh/1111"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="ايرور$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/vipabh/7"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="بوربه$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/vipabh/1159"
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="نية$"))
async def vipabh(abhvip):
  Jep = await reply_id(abhvip)
  url = f"https://t.me/vipabh/1157
  await abhvip.client.send_file(abhvip.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await abhvip.delete()
