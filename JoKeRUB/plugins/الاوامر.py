# WRITE  BY JoKeRUB
# PLUGIN FOR JoKeRUB 
# @jepthon

from telethon import events
import random, re
from ..Config import Config

from JoKeRUB.utils import admin_cmd

import asyncio
from JoKeRUB import l313l
from random import choice

from ..core.managers import edit_or_reply
from ..sql_helper.globals import gvarstatus

plugin_category = "extra"

rehu = [
    "قال المهدي(عجل الله فرجه):الدّينُ لمحمّد صلى الله عليه وآله وسلم والهدايةُ لعَلِيٍّ أمير المؤمنين ع، لأنها لهُ وفي عَقِبِه باقيةً إلى يومِ القيامة",
    "قال المهدي(عجل الله فرجه):إذا استغفرت الله (عز وجل) فالله يغفر لك",
    "قال المهدي(عجل الله فرجه):لا يحلّ لأحد أن يتصرّف في مال غيره بغير إذنه",
    "قال المهدي(عجل الله فرجه):إن اُستَرشدت أُرشِدتَ، وإن طَلبت وجدت",
    "قَالَ الإمام علي (عليه السلام): يَا ابْنَ آدَمَ إِذَا رَأَيْتَ رَبَّكَ سُبْحَانَهُ يُتَابِعُ عَلَيْكَ نِعَمَهُ وَأَنْتَ تَعْصِيهِ فَاحْذَرْهُ",
    "قَالَ الإمام علي (عليه السلام): الصَّبْرُ صَبْرَانِ صَبْرٌ عَلَى مَا تَكْرَهُ وَصَبْرٌ عَمَّا تُحِبُّ",
    "قَالَ الإمام علي (عليه السلام): لَا يَكُونُ الصَّدِيقُ صَدِيقاً حَتَّى يَحْفَظَ أَخَاهُ فِي ثَلَاثٍ فِي نَكْبَتِهِ وَغَيْبَتِهِ وَوَفَاتِهِ",
    "قال الإمام الصادق(عليه السلام): اكتبوا فإنكم لا تحفظون حتى تكتبو",
    "قال الإمام الصادق(عليه السلام): ركعة يصليها الفقيه أفضل من سبعين ألف ركعة يصليها العابد",
    "قال الإمام الصادق(عليه السلام): طلب العلم فريضة من فرائض الله",
    "عن رسول الله (صلى الله عليه وآله): الْبَخِيلُ‏ حَقّاً مَنْ ذُكِرْتُ عِنْدَهُ فَلَمْ يُصَلِّ عَلَيَّ",
    "عن رسول الله (صلى الله عليه وآله): مَنْ أَتَانِي زَائِراً كُنْتُ شَفِيعَهُ‏ يَوْمَ‏ الْقِيَامَة",
    "عن رسول الله (صلى الله عليه وآله): بُغْضُ‏ عَلِيٍ‏ كُفْرٌ وَ بُغْضُ بَنِي هَاشِمٍ نِفَاقٌ",
    "عن الامام علي (عليه السلام) قال : أعظم الذنوب ما استخف به صاحبه",
    "عن الامام علي (عليه السلام) قال : إذا قويت فاقو على طاعة الله، وإذا ضعفت فاضعف في معصيته",
    "عن الامام علي (عليه السلام) قال : أعداؤك ثلاثة: عدوك، وصديق عدوك، وعدو صديقك",
    "عن الامام علي (عليه السلام) قال : لا غنى كالعقل، ولا فقر كالجهل، ولا ميراث كالأدب",
    "عن الامام علي (عليه السلام) قال : لسانك حصانك، إن صنته صانك",
]
@l313l.ar_cmd(pattern="الاوامر(?:\s|$)([\s\S]*)")
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        lMl10l = random.choice(rehu)
        await event.edit(
        f": **⦑ قائمة الاوامر ⦒**\n★•┉ ┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n( `.م1` )  ⦙ **اوامر الادمن**\n( `.م2` )  ⦙ **اوامر المجموعة**\n( `.م3` )  ⦙ **اوامر الترحيب والردود**\n( `.م4` )  ⦙ **حماية خاص والتلكراف**\n( `.م5` )  ⦙ **اوامر المنشن والانتحال**\n( `.م6` )  ⦙ **اوامر التحميل والترجمة**\n( `.م7` )  ⦙ **اوامر المنع و القفل**\n( `.م8` )  ⦙ **اوامر التنظيف والتكرار**\n( `.م9` )  ⦙ **اوامر التخصيص والفارات**\n( `.م10` ) ⦙ **اوامر الوقتي و التشغيل**\n( `.م11` ) ⦙ **اوامر الكشف و الروابط**\n( `.م12` ) ⦙ **اوامر المساعدة والإذاعة** \n( `.م13` ) ⦙ **اوامر الارسال والاذكار**\n( `.م14` ) ⦙ **اوامر المـلصقات وكوكل**\n( `.م15` ) ⦙ **اوامر التسلية والميمز والتحشيش** \n( `.م16` ) ⦙ **اوامر الصيغ والجهات**\n( `.م17` ) ⦙ **اوامر التمبلر والزغرفة والمتحركة**\n( `.م18` ) ⦙ **اوامر الحساب والترفيه**\n( `.م19` ) ⦙ **اوامر الميوزك والتشغيل**\n( `.م20` ) ⦙ **اوامر بصمات الميمز**\n( `.م21` ) ⦙ **اوامر تجميع النقاط وبوت وعد**\n★•┉ ┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n **᯽︙ {lMl10l} **"
)

@l313l.ar_cmd(
    pattern="م1$",
    command=("م1", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الادمن للسورس  **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الحظر` )\n- ( `.اوامر الكتم` )\n- ( `.اوامر التثبيت` )\n- ( `.اوامر الاشراف` )\n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @jepthon"
)
		
@l313l.ar_cmd(
    pattern="م2$",
    command=("م2", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر المجـموعه للسورس  **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التفليش` )\n- ( `.اوامر المحذوفين` )\n- ( `.اوامر الكروب` )\n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @jepthon"
)

@l313l.ar_cmd(
    pattern="م3$",
    command=("م3", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الـترحيب والـردود **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الترحيب` )\n- ( `.اوامر الردود` )\n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @jepthon"
)
@l313l.ar_cmd(
    pattern="م4$",
    command=("م4", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر حـماية الخاص والتلكراف **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الحماية` )\n- ( `.اوامر التلكراف` ) \n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @jepthon"
)
@l313l.ar_cmd(
    pattern="م5$",
    command=("م5", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الـمنشن والانتحال **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الانتحال` )\n- ( `.اوامر التقليد` )\n- ( `.اوامر المنشن` ) \n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @jepthon"
)

@l313l.ar_cmd(
    pattern="م6$",
    command=("م6", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر التحميل والترجمه **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر النطق` )\n- ( `.اوامر التحميل` )\n- ( `.اوامر الترجمة` ) \n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @jepthon"
)

@l313l.ar_cmd(
    pattern="م7$",
    command=("م7", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر القفل والمنع **:\n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر القفل` )\n- ( `.اوامر الفتح` )\n- ( `.اوامر المنع` ) \n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @jepthon"
)

@l313l.ar_cmd(
    pattern="م8$",
    command=("م8", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر التكرار والتنظيف **:\n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التكرار` )\n- ( `.اوامر السبام` )\n- ( `.اوامر التنظيف` ) \n- ( `.اوامر المسح` ) \n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @jepthon"
)

@l313l.ar_cmd(
    pattern="م9$",
    command=("م9", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة التخصيص والفارات **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التخصيص` )\n لتغير الصور والكلايش كل من الحماية والفحص والبنك\n- ( `.اوامر الفارات` )\n - لتغير الاسم وزخرفة الوقت والصورة الوقتية والمنطقة الزمنية ورمز الاسم والبايو الوقتي وغيرها\n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @jepthon"
		)

@l313l.ar_cmd(
    pattern="م10$",
    command=("م10", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الوقتي والتشغيل **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الاسم` )\n- ( `.اوامر البايو` )\n- ( `.اوامر الكروب الوقتي` )\n- ( `.اوامر التشغيل` ) \n- ( `.اوامر الاطفاء` ) \n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @jepthon"
)	

@l313l.ar_cmd(
    pattern="م11$",
    command=("م11", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الكـشف و الروابط **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الكشف` )\n- ( `.اوامر الروابط` ) \n\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @jepthon"
)
@l313l.ar_cmd(
    pattern="م12$",
    command=("م12", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر المساعدة  **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الوقت والتاريخ` )\n- ( `.اوامر كورونا` )\n- ( `.اوامر الصلاة` ) \n- ( `.اوامر مساعدة` )\n- ( `.اوامر الاذاعه` ) \n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @jepthon"
)
@l313l.ar_cmd(
    pattern="م13$",
    command=("م13", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الارسال **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.امر الصورة الذاتية` )\n- ( `.اوامر التحذيرات` )\n- ( `.اوامر اللستة` )\n- ( `.اوامر الملكية` ) \n- ( `.اوامر السليب` ) \n- ( `.اوامر الاذكار` )\n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @jepthon"
)
@l313l.ar_cmd(
    pattern="م14$",
    command=("م14", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الملصقات وكوكل **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الملصقات` )\n- ( `.اوامر كوكل` )\n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @jepthon"
)

@l313l.ar_cmd(
    pattern="م15$",
    command=("م15", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر التسلية والتحشيش **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التسلية` )\n- ( `.اوامر التحشيش` )\n- ( `.اوامر الميمز` )\n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @jepthon"
)

@l313l.ar_cmd(
    pattern="م16$",
    command=("م16", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر تحويل الصيغ و الجهات **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التحويل` )\n- ( `.اوامر الجهات` ) \n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @jepthon"
)

@l313l.ar_cmd(
    pattern="م18$",
    command=("م18", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الحساب و الترفيه **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الترفيه` )\n- ( `.اوامر الحساب` ) \n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @jepthon"

)

@l313l.ar_cmd(
    pattern="م19",
    command=("م19", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        " قائمة اوامر الميوزك والتشغيل 🎵\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n᯽︙ اختر احدى هذه الاوامر\n ᯽︙ قبل أستخدام هذه الاوامر يجب تفعيل المود بكتابة ألامر ( `.ميوزك تفعيل` ) \n- ( `.تشغيل_المكالمة` )\n- لتشغيل المحادثة الصوتيه\n- ( `.انهاء_المكالمة` )\n-لأنهاء المحادثه الصوتية \n- ( `.دعوة` )\n- بالرد على الشخص لدعوته الى المكالمة \n- ( `.معلومات_المكالمة` )\n- لعرض عنوان المكالمة وعدد لاشخاص الموجودين فيها \n- ( `.تسمية_المكالمة` )\n- لتغير عنوان المكالمة \n- ( `.انضمام` )\n- للأنضمام الى المحادثة الصوتية\n- ( `.مغادرة` )\n- لمغادرة المحادثة الصوتية \n- ( `.تشغيل` )\n-بالرد على رابط اليوتيوب او كتابة الامر مع رابط ليوتيوب لتشغيل الاغنيه \n- ( `.قائمة_التشغيل` )\n- لعرض قائمة التشغيل \n- ( `.ايقاف_مؤقت` )\n - لأيقاف الاغنية الحالية مؤقتا \n- ( `.استمرار` )\n -لأستمرار الاغنيه التي تم ايقافها \n- ( `.تخطي` )\n- لتخطي الاغنيه وتشغيل الاغنيه الموجوده في قائمة التشغيل \n\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @jepthon"



)

@l313l.ar_cmd(
    pattern="م20$",
    command=("م20", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر بصمات الميمز **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.بصمات ميمز` )\n- ( `.بصمات ميمز2` )\n- ( `.بصمات ميمز3` )\n- ( `.بصمات ميمز4` )\n- ( `.بصمات ميمز5` )\n- ( `.بصمات انمي` ) \n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @jepthon"

)

@l313l.ar_cmd(
    pattern="م21$",
    command=("م21", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "** قائمة اوامر تجميع النقاط و بوت وعد **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التجميع` ) \n- ( `.اوامر وعد` ) \n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @jepthon"
        )
@l313l.ar_cmd(
    pattern="زيارة عاشوراء$",
    command=("زيارة عاشوراء", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("اَلسَّلامُ عَلَيْكَ يَا أَبَا عَبْدِ اللهِ ، اَلسَّلامُ عَلَيْكَ يَا بْنَ رَسُولِ اللهِ (اَلسَّلامُ عَلَيْكَ يَا خِيَرَةَ اللهِ وَابْنَ خِيَرَتِهِ ) اَلسَّلامُ عَلَيْكَ يَا بْنَ أَميرِ الْمُؤْمِنِينَ وَابْنَ سَيِّدِ الْوَصِيِّينَ ، اَلسَّلامُ عَلَيْكَ يَا بْنَ فاطِمَةَ سَيِّدَةِ نِسَاءِ الْعَالَمِينَ ، اَلسَّلامُ عَلَيْكَ يَا ثَأْرَ اللهِ وَابْنَ ثَأْرِهِ وَالْوِتْرَ الْمَوْتُورَ ، اَلسَّلامُ عَلَيْكَ وَعَلَى الْأَرْوَاحِ الَّتِي حَلَّتْ بِفِنَائِكَ ، عَلَيْكُم مِّنِّي جَمِيعاً سَلامُ اللهِ أَبَداً مَّا بَقِيتُ وَبَقِيَ اللَّيْلُ وَالنَّهَارُ ، يَا أَبَا عَبْدِ اللهِ لَقَدْ عَظُمَتِ الرَّزِيَّةُ وَجَلَّتْ ، وَعَظُمَتِ الْمُصِيبَةُ بِكَ عَلَيْنا وَعَلَى جَمِيعِ أَهْلِ الْإِسْلَامِ ، وَجَلَّتْ وَعَظُمَتْ مُصِيبَتُكَ فِي السَّمَاوَاتِ عَلَى جَمِيعِ أَهْلِ السَّمَاوَاتِ ، فَلَعَنَ اللهُ أُمَّةً أَسَّسَتْ أَسَاسَ الظُّلْمِ وَالْجَوْرِ عَلَيْكُمْ أَهْلَ الْبَيْتِ ، وَلَعَنَ اللهُ أُمَّةً دَفَعَتْكُمْ عَن مَّقامِكُمْ وَأَزالَتْكُمْ عَن مَّراتِبِكُمُ الَّتي رَتَّبَكُمُ اللهُ فِيهَا ، وَلَعَنَ اللهُ أُمَّةً قَتَلَتْكُمْ وَلَعَنَ اللهُ الْمُمَهِّدِينَ لَهُمْ بِالتَّمْكِينِ مِنْ قِتَالِكُمْ ، بَرِئْتُ إِلَى اللهِ وَإِلَيْكُمْ مِنْهُمْ وَمِنْ أَشْيَاعِهِمْ وَأَتْبَاعِهِمْ وَأَوْلِيَائِهِم ، يَا أَبَا عَبْدِ اللهِ إِنِّي سِلْمٌ لِمَنْ سَالَمَكُمْ وَحَرْبٌ لِّمَنْ حَارَبَكُمْ إِلَى يَوْمِ الْقِيَامَةِ ، وَلَعَنَ اللهُ آلَ زِيَادٍ وَّآلَ مَرْوَانَ ، وَلَعَنَ اللهُ بَنِي أُمَيَّةَ قَاطِبَةً ، وَّلَعَنَ اللهُ ابْنَ مَرْجَانَةَ ، وَلَعَنَ اللهُ عُمَرَ بْنَ سَعْدٍ ، وَّلَعَنَ اللهُ شِمْراً ، وَّلَعَنَ اللهُ أُمَّةً أَسْرَجَتْ وَأَلْجَمَتْ وَتَنَقَّبَتْ لِقِتَالِكَ ، بِأَبِي أَنْتَ وَأُمِّي لَقَدْ عَظُمَ مُصَابِي بِكَ ، فَأَسْأَلُ اللهَ الَّذِي أَكْرَمَ مَقَامَكَ وَأَكْرَمَنِي بِكَ أَن يَّرْزُقَنِي طَلَبَ ثَأْرِكَ مَعَ إِمَامٍ مَّنْصُورٍ مِنْ أَهْلِ بَيْتِ مُحَمَّدٍ ـ صَلَّى اللهُ عَلَيْهِ وَآلِهِ ـ ، اَللَّهُمَّ اجْعَلْنِي عِنْدَكَ وَجيهاً بِالْحُسَيْنِ ـ عَلَيْهِ السَّلامُ ـ فِي الدُّنْيَا وَالْآخِرَةِ ، يَا أَبَا عَبْدِ اللهِ إِنِّي أَتَقَرَّبُ إِلى اللهِ وَإِلَى رَسُولِهِ وَإِلَى أَمِيرِ الْمُؤْمِنِينَ وَإِلَى فَاطِمَةَ وَإِلَى الْحَسَنِ وَإِلَيْكَ بِمُوَالاتِكَ وَبِالْبَرَاءَةِ [ مِمَّنْ قَاتَلَكَ وَنَصَبَ لَكَ الْحَرْبَ وَبِالْبَراءَةِ مِمَّنْ أَسَّسَ أَسَاسَ الظُّلْمِ وَالْجَوْرِ عَلَيْكُمْ وَأَبْرَأُ إِلَى اللهِ وَإِلَى رَسُولِهِ ] مِمَّنْ أَسَّسَ أَسَاسَ ذَلِكَ وَبَنَى عَلَيْهِ بُنْيَانَهُ وَجَرى فِي ظُلْمِهِ وَجَوْرِهِ عَلَيْكُمْ وَعَلَى أَشْيَاعِكُمْ ، بَرِئْتُ إِلَى اللهِ وَإِلَيْكُم مَِنْهُمْ ، وَأَتَقَرَّبُ إِلَى اللهِ ثُمَّ إِلَيْكُمْ بِمُوَالاتِكُمْ وَمُوَالاةِ وَلِيِّكُمْ وَبِالْبَرَاءَةِ مِنْ أَعْدَائِكُمْ وَالنَّاصِبِينَ لَكُمُ الْحَرْبَ وَبِالْبَرَاءَةِ مِنْ أَشْيَاعِهِمْ وَأَتْبَاعِهِمْ ، إِنِّي سِلْمٌ لِّمَنْ سَالَمَكُمْ وَحَرْبٌ لِّمَنْ حَارَبَكُمْ وَوَلِيٌّ لِّمَنْ وَالاكُمْ وَعَدُوٌّ لَِمَنْ عَادَاكُمْ ، فَأَسْأَلُ اللهَ الَّذِي أَكْرَمَنِي بِمَعْرِفَتِكُمْ وَمَعْرِفَةِ أَوْلِيَائِكُمْ وَرَزَقَنِيَ الْبَرَاءَةَ مِنْ أَعْدَائِكُمْ أَن يَّجْعَلَنِي مَعَكُمْ فِي الدُّنْيا وَالْآخِرَةِ ، وَأَن يُّثَبِّتَ لِي عِنْدَكُمْ قَدَمَ صِدْقٍ فِي الدُّنْيا وَالْآخِرَةِ ، وَأَسْأَلُهُ أَن يُّبَلِّغَنِيَ الْمَقَامَ الْمَحْمُودَ لَكُمْ عِنْدَ اللهِ ، وَأَن يَّرْزُقَني طَلَبَ ثَأْرِي مَعَ إِمَامِ هُدًى ظَاهِرٍ نَّاطِقٍ بِالْحَقِّ مِنْكُمْ ، وَأَسْألُ اللهَ بِحَقِّكُمْ وَبِالشَّأْنِ الَّذِي لَكُمْ عِنْدَهُ أَنْ يُعْطِيَنِي بِمُصَابِي بِكُمْ أَفْضَلَ مَا يُعْطِي مُصَاباً بِمُصِيبَتِهِ ، مُصِيبَةً مَّا أَعْظَمَهَا وَأَعْظَمَ رَزِيَّتَهَا فِي الْإِسْلامِ وَفِي جَمِيعِ السَّمَاوَاتِ وَالْأرْضِ ، اَللَّـهُمَّ اجْعَلْنِي فِي مَقَامِي هَذَا مِمَّنْ تَنَالُهُ مِنْكَ صَلَوَاتٌ وَّرَحْمَةٌ وَّمَغْفِرَةٌ ، اَللَّـهُمَّ اجْعَلْ مَحْيَايَ مَحْيَا مُحَمَّدٍ وَّآلِ مُحَمَّدٍ ، وَّمَمَاتِي مَمَاتَ مُحَمَّدٍ وََآلِ مُحَمَّدٍ ، اَللّّـهُمَّ إِنَّ هَذَا يَوْمٌ تَبَرَّكَتْ بِهِ بَنُو أُمَيَّةَ وَابْنُ آكِلَةِ الْأَكْبَادِ اللَّعِينُ بْنُ اللَّعِينِ عَلَى لِسَانِكَ وَلِسَانِ نَبِيِّكَ ـ صَلَّى اللهُ عَلَيْهِ وَآلِهِ ـ فِي كُلِّ مَوْطِنٍ وَّمَوْقِفٍ وَّقَفَ فِيهِ نَبِيُّكَ ـ صَلَّى اللهُ عَلَيْهِ وَآلِهِ ـ ، اَللَّـهُمَّ الْعَنْ أَبَا سُفْيَانَ وَمُعَاوِيَةَ وَيَزيدَ بْنَ مُعَاوِيَةَ عَلَيْهِم مِّنْكَ اللَّعْنَةُ أَبَدَ الْآبِدِينَ ، وَهَذَا يَوْمٌ فَرِحَتْ بِهِ آلُ زِيَادٍ وَآلُ مَرْوَانَ بِقَتْلِهِمُ الْحُسَيْنَ ـ صَلَواتُ اللهِ عَلَيْهِ ـ ، اَللَّـهُمَّ فَضَاعِفْ عَلَيْهِمُ اللَّعْنَ مِنْكَ وَالْعَذَابَ الْأَلِيمَ ، اَللَّـهُمَّ إِنِّي أَتَقَرَّبُ إِلَيْكَ فِي هَذَا الْيَوْمِ وَفِي مَوْقِفِي هَذَا وَأَيَّامِ حَيَاتِي بِالْبَرَاءَةِ مِنْهُمْ وَاللَّعْنَةِ عَلَيْهِمْ وَبِالْمُوَالاةِ لِنَبِيِّكَ وَآلِ نَبِيِّكَ ـ عَلَيْهِ وَعَلَيْهِمُ السَّلامُ ـ . ثمّ تقول مائة مرّة : اَللَّـهُمَّ الْعَنْ أَوَّلَ ظَالِمٍ ظَلَمَ حَقَّ مُحَمَّدٍ وَّآلِ مُحَمَّدٍ وَآخِرَ تَابِعٍ لَهُ عَلَى ذلِكَ ، اَللّـَهُمَّ الْعَنِ الْعِصَابَةَ الَّتي جَاهَدَتِ الْحُسَيْنَ ـ عَلَيْهِ السَّلَامُ ـ وَشَايَعَتْ وَبَايَعَتْ وَتَابَعَتْ عَلَى قَتْلِهِ ، اَللَّـهُمَّ الْعَنْهُمْ جَمِيعاً . ثمّ تقول مائة مرّة : اَلسَّلامُ عَلَيْكَ يَا أَبَا عَبْدِ اللهِ وَعَلَى الْأَرْوَاحِ الَّتِي حَلَّتْ بِفِنَائِكَ ، عَلَيْكَ مِنِّي سَلامُ اللهِ أَبَداً مَّا بَقِيتُ وَبَقِيَ اللَّيْلُ وَالنَّهَارُ ، وَلا جَعَلَهُ اللهُ آخِرَ الْعَهْدِ مِنِّي لِزِيَارَتِكُمْ ، اَلسَّلامُ عَلَى الْحُسَيْنِ ، وَعَلَى عَلِيِّ بْنِ الْحُسَيْنِ وَعَلَى أَوْلادِ الْحُسَيْنِ وَعَلَى أَصْحَابِ الْحُسَيْنِ . ثمّ تقول : اَللَّـهُمَّ خُصَّ أَنْتَ أَوَّلَ ظَالِمٍ بِاللَّعْنِ مِنِّي ، وَابْدَأْ بِهِ أَوَّلاً ، ثُمَّ الْعَنِ الثَّانيَ وَالثَّالِثَ وَالرَّابِعَ ، اَللّـَهُمَّ الْعَنْ يَزيدَ خَامِساً ، وَالْعَنْ عُبَيْدَ اللهِ بْنَ زِيَادٍ وَّابْنَ مَرْجانَةَ وَعُمَرَ بْنَ سَعْدٍ وَّشِمْراً وَآلَ أَبِي سُفْيَانَ وَآلَ زِيادٍ وََآلَ مَرْوَانَ إِلَى يَوْمِ الْقِيَامَةِ . ثمّ تسجد وتقُول : اَللَّـهُمَّ لَكَ الْحَمْدُ حَمْدَ الشَّاكِرِينَ لَكَ عَلَى مُصَابِهِمْ ، اَلْحَمْدُ للهِ عَلَى عَظِيمِ رَزِيَّتِي ، اَللَّـهُمَّ ارْزُقْنِي شَفَاعَةَ الْحُسَيْنِ يَوْمَ الْوُرُودِ ، وَثَبِّتْ لِي قَدَمَ صِدْقٍ عِنْدَكَ مَعَ الْحُسَيْنِ وَأَصْحَابِ الْحُسَيْنِ اَلَّذِينَ بَذَلُوا مُهَجَهُمْ دُونَ الْحُسَيْنِ عَلَيْهِ السَّلامُ")
