""" Command: اوقات الصلاة لعواصم الدول باللغـة العربيـة
Credit: @Tepthon
@zzzzl1l - كتـابـة الملـف :  زلــزال الهيبــه"""

import json
import requests
from Tepthon import zedub
from Tepthon.core.logger import logging

from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply

plugin_category = "البحث"

@zedub.zed_cmd(
    pattern="صلاة ([\s\S]*)",
    command=("صلاة", plugin_category),
    info={
        "header": "أوقـات الصـلاة لـ عواصـم الـدول العـربيـة",
        "الاستـخـدام": "{tr}صلاة + العاصمـة",
    },
)
async def get_adzan(adzan):
    ZELZAL = adzan.pattern_match.group(1)
    if ZELZAL == "صنعاء" or ZELZAL == "اليمن":
	    url = f"http://api.aladhan.com/v1/timingsByCity?city=Sanaa"
	    request = requests.get(url)
	    if request.status_code != 200:
	        await edit_delete(
	            adzan,
	            f"** لم يـتم العثور على هـذه المدينة {ZELZAL}**\n**-يرجى كتابة اسم العاصمـه او الدولـة بشكـل صحيـح** ",
	            5,
	        )
	        return
	    result = json.loads(request.text)
	    zedthonresult = f"<b>🕋╎أوقـات الصـلاة بالتـوقيت المحلـي لعواصـم الـدول <b>\
	            \n\n<b>المـدينة     : <b>صنعـاء</b>\
	            \n<b>الـدولة  : <b>اليمـن</b>\
	            \n<b>التـاريخ     : <b>{result['results']['datetime'][0]['date']['gregorian']}</b>\
	            \n<b>الهـجري    : <b>{result['results']['datetime'][0]['date']['hijri']}</b>\
	            \n\n<b>الإمسـاك    : <b>{result['results']['datetime'][0]['times']['Imsak']}</b>\
	            \n<b>شـروق الشمس  : <b>{result['results']['datetime'][0]['times']['Sunrise']}</b>\
	            \n<b>الـفجر     : <b>{result['results']['datetime'][0]['times']['Fajr']}</b>\
	            \n<b>الظـهر    : <b>{result['results']['datetime'][0]['times']['Dhuhr']}</b>\
	            \n<b>العـصر      : <b>{result['results']['datetime'][0]['times']['Asr']}</b>\
	            \n<b>غـروب الشمس   : <b>{result['results']['datetime'][0]['times']['Sunset']}</b>\
	            \n<b>المـغرب  : <b>{result['results']['datetime'][0]['times']['Maghrib']}</b>\
	            \n<b>العشـاء     : <b>{result['results']['datetime'][0]['times']['Isha']}</b>\
	            \n<b>منتـصف الليل : <b>{result['results']['datetime'][0]['times']['Midnight']}</b>\
		        \n\nᯓ 𝗦𝗢𝗨𝗥𝗖𝗘 𝗧𝗘𝗣𝗧𝗛𝗢𝗡╎@Tepthon\
	    "
	    await edit_or_reply(adzan, zedthonresult, "html")
    elif ZELZAL == "مصر" or ZELZAL == "القاهرة" or ZELZAL == "القاهره":
	    url = f"http://api.aladhan.com/v1/timingsByCity?city=Cairo"
	    request = requests.get(url)
	    if request.status_code != 200:
	        await edit_delete(
	            adzan,
	            f"** لم يـتم العثور على هـذه المدينة {ZELZAL}**\n**-يرجى كتابة اسم العاصمـه او الدولـة بشكـل صحيـح** ",
	            5,
	        )
	        return
	    result = json.loads(request.text)
	    zedthonresult = f"<b>🕋╎أوقـات الصـلاة بالتـوقيت المحلـي لعواصـم الـدول <b>\
	            \n\n<b>المـدينة     : <b>القاهـرة</b>\
	            \n<b>الـدولة  : <b>مصـر</b>\
	            \n<b>التـاريخ     : <b>{result['results']['datetime'][0]['date']['gregorian']}</b>\
	            \n<b>الهـجري    : <b>{result['results']['datetime'][0]['date']['hijri']}</b>\
	            \n\n<b>الإمسـاك    : <b>{result['results']['datetime'][0]['times']['Imsak']}</b>\
	            \n<b>شـروق الشمس  : <b>{result['results']['datetime'][0]['times']['Sunrise']}</b>\
	            \n<b>الـفجر     : <b>{result['results']['datetime'][0]['times']['Fajr']}</b>\
	            \n<b>الظـهر    : <b>{result['results']['datetime'][0]['times']['Dhuhr']}</b>\
	            \n<b>العـصر      : <b>{result['results']['datetime'][0]['times']['Asr']}</b>\
	            \n<b>غـروب الشمس   : <b>{result['results']['datetime'][0]['times']['Sunset']}</b>\
	            \n<b>المـغرب  : <b>{result['results']['datetime'][0]['times']['Maghrib']}</b>\
	            \n<b>العشـاء     : <b>{result['results']['datetime'][0]['times']['Isha']}</b>\
	            \n<b>منتـصف الليل : <b>{result['results']['datetime'][0]['times']['Midnight']}</b>\
		        \n\nᯓ 𝗦𝗢𝗨𝗥𝗖𝗘 𝗧𝗘𝗣𝗧𝗛𝗢𝗡╎@Tepthon\
	    "
	    await edit_or_reply(adzan, zedthonresult, "html")
    elif ZELZAL == "بغداد" or ZELZAL == "العراق":
	    url = f"http://api.aladhan.com/v1/timingsByCity?city=Baghdad"
	    request = requests.get(url)
	    if request.status_code != 200:
	        await edit_delete(
	            adzan,
	            f"** لم يـتم العثور على هـذه المدينة {ZELZAL}**\n**-يرجى كتابة اسم العاصمـه او الدولـة بشكـل صحيـح** ",
	            5,
	        )
	        return
	    result = json.loads(request.text)
	    zedthonresult = f"<b>🕋╎أوقـات الصـلاة بالتـوقيت المحلـي لعواصـم الـدول <b>\
	            \n\n<b>المـدينة     : <b>بغـداد</b>\
	            \n<b>الـدولة  : <b>العـراق</b>\
	            \n<b>التـاريخ     : <b>{result['results']['datetime'][0]['date']['gregorian']}</b>\
	            \n<b>الهـجري    : <b>{result['results']['datetime'][0]['date']['hijri']}</b>\
	            \n\n<b>الإمسـاك    : <b>{result['results']['datetime'][0]['times']['Imsak']}</b>\
	            \n<b>شـروق الشمس  : <b>{result['results']['datetime'][0]['times']['Sunrise']}</b>\
	            \n<b>الـفجر     : <b>{result['results']['datetime'][0]['times']['Fajr']}</b>\
	            \n<b>الظـهر    : <b>{result['results']['datetime'][0]['times']['Dhuhr']}</b>\
	            \n<b>العـصر      : <b>{result['results']['datetime'][0]['times']['Asr']}</b>\
	            \n<b>غـروب الشمس   : <b>{result['results']['datetime'][0]['times']['Sunset']}</b>\
	            \n<b>المـغرب  : <b>{result['results']['datetime'][0]['times']['Maghrib']}</b>\
	            \n<b>العشـاء     : <b>{result['results']['datetime'][0]['times']['Isha']}</b>\
	            \n<b>منتـصف الليل : <b>{result['results']['datetime'][0]['times']['Midnight']}</b>\
		        \n\nᯓ 𝗦𝗢𝗨𝗥𝗖𝗘 𝗧𝗘𝗣𝗧𝗛𝗢𝗡╎@Tepthon\
	    "
	    await edit_or_reply(adzan, zedthonresult, "html")
    elif ZELZAL == "دمشق" or ZELZAL == "سوريا":
	    url = f"http://api.aladhan.com/v1/timingsByCity?city=Damascus"
	    request = requests.get(url)
	    if request.status_code != 200:
	        await edit_delete(
	            adzan,
	            f"** لم يـتم العثور على هـذه المدينة {ZELZAL}**\n**-يرجى كتابة اسم العاصمـه او الدولـة بشكـل صحيـح** ",
	            5,
	        )
	        return
	    result = json.loads(request.text)
	    zedthonresult = f"<b>🕋╎أوقـات الصـلاة بالتـوقيت المحلـي لعواصـم الـدول <b>\
	            \n\n<b>المـدينة     : <b>دمشـق</b>\
	            \n<b>الـدولة  : <b>سـوريا</b>\
	            \n<b>التـاريخ     : <b>{result['results']['datetime'][0]['date']['gregorian']}</b>\
	            \n<b>الهـجري    : <b>{result['results']['datetime'][0]['date']['hijri']}</b>\
	            \n\n<b>الإمسـاك    : <b>{result['results']['datetime'][0]['times']['Imsak']}</b>\
	            \n<b>شـروق الشمس  : <b>{result['results']['datetime'][0]['times']['Sunrise']}</b>\
	            \n<b>الـفجر     : <b>{result['results']['datetime'][0]['times']['Fajr']}</b>\
	            \n<b>الظـهر    : <b>{result['results']['datetime'][0]['times']['Dhuhr']}</b>\
	            \n<b>العـصر      : <b>{result['results']['datetime'][0]['times']['Asr']}</b>\
	            \n<b>غـروب الشمس   : <b>{result['results']['datetime'][0]['times']['Sunset']}</b>\
	            \n<b>المـغرب  : <b>{result['results']['datetime'][0]['times']['Maghrib']}</b>\
	            \n<b>العشـاء     : <b>{result['results']['datetime'][0]['times']['Isha']}</b>\
	            \n<b>منتـصف الليل : <b>{result['results']['datetime'][0]['times']['Midnight']}</b>\
		        \n\nᯓ 𝗦𝗢𝗨𝗥𝗖𝗘 𝗧𝗘𝗣𝗧𝗛𝗢𝗡╎@Tepthon\
	    "
	    await edit_or_reply(adzan, zedthonresult, "html")
    elif ZELZAL == "الدوحه" or ZELZAL == "قطر":
	    url = f"http://api.aladhan.com/v1/timingsByCity?city=Doha"
	    request = requests.get(url)
	    if request.status_code != 200:
	        await edit_delete(
	            adzan,
	            f"** لم يـتم العثور على هـذه المدينة {ZELZAL}**\n**-يرجى كتابة اسم العاصمـه او الدولـة بشكـل صحيـح** ",
	            5,
	        )
	        return
	    result = json.loads(request.text)
	    zedthonresult = f"<b>🕋╎أوقـات الصـلاة بالتـوقيت المحلـي لعواصـم الـدول <b>\
	            \n\n<b>المـدينة     : <b>الدوحـه</b>\
	            \n<b>الـدولة  : <b>قطـر</b>\
	            \n<b>التـاريخ     : <b>{result['results']['datetime'][0]['date']['gregorian']}</b>\
	            \n<b>الهـجري    : <b>{result['results']['datetime'][0]['date']['hijri']}</b>\
	            \n\n<b>الإمسـاك    : <b>{result['results']['datetime'][0]['times']['Imsak']}</b>\
	            \n<b>شـروق الشمس  : <b>{result['results']['datetime'][0]['times']['Sunrise']}</b>\
	            \n<b>الـفجر     : <b>{result['results']['datetime'][0]['times']['Fajr']}</b>\
	            \n<b>الظـهر    : <b>{result['results']['datetime'][0]['times']['Dhuhr']}</b>\
	            \n<b>العـصر      : <b>{result['results']['datetime'][0]['times']['Asr']}</b>\
	            \n<b>غـروب الشمس   : <b>{result['results']['datetime'][0]['times']['Sunset']}</b>\
	            \n<b>المـغرب  : <b>{result['results']['datetime'][0]['times']['Maghrib']}</b>\
	            \n<b>العشـاء     : <b>{result['results']['datetime'][0]['times']['Isha']}</b>\
	            \n<b>منتـصف الليل : <b>{result['results']['datetime'][0]['times']['Midnight']}</b>\
		        \n\nᯓ 𝗦𝗢𝗨𝗥𝗖𝗘 𝗧𝗘𝗣𝗧𝗛𝗢𝗡╎@Tepthon\
	    "
	    await edit_or_reply(adzan, zedthonresult, "html")
    elif ZELZAL == "مسقط" or ZELZAL == "سلطنه عمان":
	    url = f"http://api.aladhan.com/v1/timingsByCity?city=Muscat"
	    request = requests.get(url)
	    if request.status_code != 200:
	        await edit_delete(
	            adzan,
	            f"** لم يـتم العثور على هـذه المدينة {ZELZAL}**\n**-يرجى كتابة اسم العاصمـه او الدولـة بشكـل صحيـح** ",
	            5,
	        )
	        return
	    result = json.loads(request.text)
	    zedthonresult = f"<b>🕋╎أوقـات الصـلاة بالتـوقيت المحلـي لعواصـم الـدول <b>\
	            \n\n<b>المـدينة     : <b>مسقـط</b>\
	            \n<b>الـدولة  : <b>سلطنـة عمـان</b>\
	            \n<b>التـاريخ     : <b>{result['results']['datetime'][0]['date']['gregorian']}</b>\
	            \n<b>الهـجري    : <b>{result['results']['datetime'][0]['date']['hijri']}</b>\
	            \n\n<b>الإمسـاك    : <b>{result['results']['datetime'][0]['times']['Imsak']}</b>\
	            \n<b>شـروق الشمس  : <b>{result['results']['datetime'][0]['times']['Sunrise']}</b>\
	            \n<b>الـفجر     : <b>{result['results']['datetime'][0]['times']['Fajr']}</b>\
	            \n<b>الظـهر    : <b>{result['results']['datetime'][0]['times']['Dhuhr']}</b>\
	            \n<b>العـصر      : <b>{result['results']['datetime'][0]['times']['Asr']}</b>\
	            \n<b>غـروب الشمس   : <b>{result['results']['datetime'][0]['times']['Sunset']}</b>\
	            \n<b>المـغرب  : <b>{result['results']['datetime'][0]['times']['Maghrib']}</b>\
	            \n<b>العشـاء     : <b>{result['results']['datetime'][0]['times']['Isha']}</b>\
	            \n<b>منتـصف الليل : <b>{result['results']['datetime'][0]['times']['Midnight']}</b>\
		        \n\nᯓ 𝗦𝗢𝗨𝗥𝗖𝗘 𝗧𝗘𝗣𝗧𝗛𝗢𝗡╎@Tepthon\
	    "
	    await edit_or_reply(adzan, zedthonresult, "html")
    elif ZELZAL == "مكة" or ZELZAL == "السعودية":
	    url = f"http://api.aladhan.com/v1/timingsByCity?city=Mecca"
	    request = requests.get(url)
	    if request.status_code != 200:
	        await edit_delete(
	            adzan,
	            f"** لم يـتم العثور على هـذه المدينة {ZELZAL}**\n**-يرجى كتابة اسم العاصمـه او الدولـة بشكـل صحيـح** ",
	            5,
	        )
	        return
	    result = json.loads(request.text)
	    zedthonresult = f"<b>🕋╎أوقـات الصـلاة بالتـوقيت المحلـي لعواصـم الـدول <b>\
	            \n\n<b>المـدينة     : <b>مكـه المكـرمـه</b>\
	            \n<b>الـدولة  : <b>المملكـة العربيـه السعـودية</b>\
	            \n<b>التـاريخ     : <b>{result['results']['datetime'][0]['date']['gregorian']}</b>\
	            \n<b>الهـجري    : <b>{result['results']['datetime'][0]['date']['hijri']}</b>\
	            \n\n<b>الإمسـاك    : <b>{result['results']['datetime'][0]['times']['Imsak']}</b>\
	            \n<b>شـروق الشمس  : <b>{result['results']['datetime'][0]['times']['Sunrise']}</b>\
	            \n<b>الـفجر     : <b>{result['results']['datetime'][0]['times']['Fajr']}</b>\
	            \n<b>الظـهر    : <b>{result['results']['datetime'][0]['times']['Dhuhr']}</b>\
	            \n<b>العـصر      : <b>{result['results']['datetime'][0]['times']['Asr']}</b>\
	            \n<b>غـروب الشمس   : <b>{result['results']['datetime'][0]['times']['Sunset']}</b>\
	            \n<b>المـغرب  : <b>{result['results']['datetime'][0]['times']['Maghrib']}</b>\
	            \n<b>العشـاء     : <b>{result['results']['datetime'][0]['times']['Isha']}</b>\
	            \n<b>منتـصف الليل : <b>{result['results']['datetime'][0]['times']['Midnight']}</b>\
		        \n\nᯓ 𝗦𝗢𝗨𝗥𝗖𝗘 𝗧𝗘𝗣𝗧𝗛𝗢𝗡╎@Tepthon\
	    "
	    await edit_or_reply(adzan, zedthonresult, "html")
    elif ZELZAL == "بيروت" or ZELZAL == "لبنان":
	    url = f"http://api.aladhan.com/v1/timingsByCity?city=Beirut"
	    request = requests.get(url)
	    if request.status_code != 200:
	        await edit_delete(
	            adzan,
	            f"** لم يـتم العثور على هـذه المدينة {ZELZAL}**\n**-يرجى كتابة اسم العاصمـه او الدولـة بشكـل صحيـح** ",
	            5,
	        )
	        return
	    result = json.loads(request.text)
	    zedthonresult = f"<b>🕋╎أوقـات الصـلاة بالتـوقيت المحلـي لعواصـم الـدول <b>\
	            \n\n<b>المـدينة     : <b>بيـروت</b>\
	            \n<b>الـدولة  : <b>لبنـان</b>\
	            \n<b>التـاريخ     : <b>{result['results']['datetime'][0]['date']['gregorian']}</b>\
	            \n<b>الهـجري    : <b>{result['results']['datetime'][0]['date']['hijri']}</b>\
	            \n\n<b>الإمسـاك    : <b>{result['results']['datetime'][0]['times']['Imsak']}</b>\
	            \n<b>شـروق الشمس  : <b>{result['results']['datetime'][0]['times']['Sunrise']}</b>\
	            \n<b>الـفجر     : <b>{result['results']['datetime'][0]['times']['Fajr']}</b>\
	            \n<b>الظـهر    : <b>{result['results']['datetime'][0]['times']['Dhuhr']}</b>\
	            \n<b>العـصر      : <b>{result['results']['datetime'][0]['times']['Asr']}</b>\
	            \n<b>غـروب الشمس   : <b>{result['results']['datetime'][0]['times']['Sunset']}</b>\
	            \n<b>المـغرب  : <b>{result['results']['datetime'][0]['times']['Maghrib']}</b>\
	            \n<b>العشـاء     : <b>{result['results']['datetime'][0]['times']['Isha']}</b>\
	            \n<b>منتـصف الليل : <b>{result['results']['datetime'][0]['times']['Midnight']}</b>\
		        \n\nᯓ 𝗦𝗢𝗨𝗥𝗖𝗘 𝗧𝗘𝗣𝗧𝗛𝗢𝗡╎@Tepthon\
	    "
	    await edit_or_reply(adzan, zedthonresult, "html")
    elif ZELZAL == "عمان" or ZELZAL == "الاردن":
	    url = f"http://api.aladhan.com/v1/timingsByCity?city=Amman"
	    request = requests.get(url)
	    if request.status_code != 200:
	        await edit_delete(
	            adzan,
	            f"** لم يـتم العثور على هـذه المدينة {ZELZAL}**\n**-يرجى كتابة اسم العاصمـه او الدولـة بشكـل صحيـح** ",
	            5,
	        )
	        return
	    result = json.loads(request.text)
	    zedthonresult = f"<b>🕋╎أوقـات الصـلاة بالتـوقيت المحلـي لعواصـم الـدول <b>\
	            \n\n<b>المـدينة     : <b>عَمـان</b>\
	            \n<b>الـدولة  : <b>الاردن</b>\
	            \n<b>التـاريخ     : <b>{result['results']['datetime'][0]['date']['gregorian']}</b>\
	            \n<b>الهـجري    : <b>{result['results']['datetime'][0]['date']['hijri']}</b>\
	            \n\n<b>الإمسـاك    : <b>{result['results']['datetime'][0]['times']['Imsak']}</b>\
	            \n<b>شـروق الشمس  : <b>{result['results']['datetime'][0]['times']['Sunrise']}</b>\
	            \n<b>الـفجر     : <b>{result['results']['datetime'][0]['times']['Fajr']}</b>\
	            \n<b>الظـهر    : <b>{result['results']['datetime'][0]['times']['Dhuhr']}</b>\
	            \n<b>العـصر      : <b>{result['results']['datetime'][0]['times']['Asr']}</b>\
	            \n<b>غـروب الشمس   : <b>{result['results']['datetime'][0]['times']['Sunset']}</b>\
	            \n<b>المـغرب  : <b>{result['results']['datetime'][0]['times']['Maghrib']}</b>\
	            \n<b>العشـاء     : <b>{result['results']['datetime'][0]['times']['Isha']}</b>\
	            \n<b>منتـصف الليل : <b>{result['results']['datetime'][0]['times']['Midnight']}</b>\
		        \n\nᯓ 𝗦𝗢𝗨𝗥𝗖𝗘 𝗧𝗘𝗣𝗧𝗛𝗢𝗡╎@Tepthon\
	    "
	    await edit_or_reply(adzan, zedthonresult, "html")
    elif ZELZAL == "الرباط" or ZELZAL == "المغرب":
	    url = f"http://api.aladhan.com/v1/timingsByCity?city=Rabat"
	    request = requests.get(url)
	    if request.status_code != 200:
	        await edit_delete(
	            adzan,
	            f"** لم يـتم العثور على هـذه المدينة {ZELZAL}**\n**-يرجى كتابة اسم العاصمـه او الدولـة بشكـل صحيـح** ",
	            5,
	        )
	        return
	    result = json.loads(request.text)
	    zedthonresult = f"<b>🕋╎أوقـات الصـلاة بالتـوقيت المحلـي لعواصـم الـدول <b>\
	            \n\n<b>المـدينة     : <b>الربـاط</b>\
	            \n<b>الـدولة  : <b>المغـرب</b>\
	            \n<b>التـاريخ     : <b>{result['results']['datetime'][0]['date']['gregorian']}</b>\
	            \n<b>الهـجري    : <b>{result['results']['datetime'][0]['date']['hijri']}</b>\
	            \n\n<b>الإمسـاك    : <b>{result['results']['datetime'][0]['times']['Imsak']}</b>\
	            \n<b>شـروق الشمس  : <b>{result['results']['datetime'][0]['times']['Sunrise']}</b>\
	            \n<b>الـفجر     : <b>{result['results']['datetime'][0]['times']['Fajr']}</b>\
	            \n<b>الظـهر    : <b>{result['results']['datetime'][0]['times']['Dhuhr']}</b>\
	            \n<b>العـصر      : <b>{result['results']['datetime'][0]['times']['Asr']}</b>\
	            \n<b>غـروب الشمس   : <b>{result['results']['datetime'][0]['times']['Sunset']}</b>\
	            \n<b>المـغرب  : <b>{result['results']['datetime'][0]['times']['Maghrib']}</b>\
	            \n<b>العشـاء     : <b>{result['results']['datetime'][0]['times']['Isha']}</b>\
	            \n<b>منتـصف الليل : <b>{result['results']['datetime'][0]['times']['Midnight']}</b>\
		        \n\nᯓ 𝗦𝗢𝗨𝗥𝗖𝗘 𝗧𝗘𝗣𝗧𝗛𝗢𝗡╎@Tepthon\
	    "
	    await edit_or_reply(adzan, zedthonresult, "html")
    elif ZELZAL == "الخرطوم" or ZELZAL == "السودان":
	    url = f"http://api.aladhan.com/v1/timingsByCity?city=Khartoum"
	    request = requests.get(url)
	    if request.status_code != 200:
	        await edit_delete(
	            adzan,
	            f"** لم يـتم العثور على هـذه المدينة {ZELZAL}**\n**-يرجى كتابة اسم العاصمـه او الدولـة بشكـل صحيـح** ",
	            5,
	        )
	        return
	    result = json.loads(request.text)
	    zedthonresult = f"<b>🕋╎أوقـات الصـلاة بالتـوقيت المحلـي لعواصـم الـدول <b>\
	            \n\n<b>المـدينة     : <b>الخرطـوم</b>\
	            \n<b>الـدولة  : <b>السـودان</b>\
	            \n<b>التـاريخ     : <b>{result['results']['datetime'][0]['date']['gregorian']}</b>\
	            \n<b>الهـجري    : <b>{result['results']['datetime'][0]['date']['hijri']}</b>\
	            \n\n<b>الإمسـاك    : <b>{result['results']['datetime'][0]['times']['Imsak']}</b>\
	            \n<b>شـروق الشمس  : <b>{result['results']['datetime'][0]['times']['Sunrise']}</b>\
	            \n<b>الـفجر     : <b>{result['results']['datetime'][0]['times']['Fajr']}</b>\
	            \n<b>الظـهر    : <b>{result['results']['datetime'][0]['times']['Dhuhr']}</b>\
	            \n<b>العـصر      : <b>{result['results']['datetime'][0]['times']['Asr']}</b>\
	            \n<b>غـروب الشمس   : <b>{result['results']['datetime'][0]['times']['Sunset']}</b>\
	            \n<b>المـغرب  : <b>{result['results']['datetime'][0]['times']['Maghrib']}</b>\
	            \n<b>العشـاء     : <b>{result['results']['datetime'][0]['times']['Isha']}</b>\
	            \n<b>منتـصف الليل : <b>{result['results']['datetime'][0]['times']['Midnight']}</b>\
		        \n\nᯓ 𝗦𝗢𝗨𝗥𝗖𝗘 𝗧𝗘𝗣𝗧𝗛𝗢𝗡╎@Tepthon\
	    "
	    await edit_or_reply(adzan, zedthonresult, "html")
    elif ZELZAL == "بنغازي" or ZELZAL == "ليبيا":
	    url = f"http://api.aladhan.com/v1/timingsByCity?city=Benghazi"
	    request = requests.get(url)
	    if request.status_code != 200:
	        await edit_delete(
	            adzan,
	            f"** لم يـتم العثور على هـذه المدينة {ZELZAL}**\n**-يرجى كتابة اسم العاصمـه او الدولـة بشكـل صحيـح** ",
	            5,
	        )
	        return
	    result = json.loads(request.text)
	    zedthonresult = f"<b>🕋╎أوقـات الصـلاة بالتـوقيت المحلـي لعواصـم الـدول <b>\
	            \n\n<b>المـدينة     : <b>بنغـازي</b>\
	            \n<b>الـدولة  : <b>ليبيـا</b>\
	            \n<b>التـاريخ     : <b>{result['results']['datetime'][0]['date']['gregorian']}</b>\
	            \n<b>الهـجري    : <b>{result['results']['datetime'][0]['date']['hijri']}</b>\
	            \n\n<b>الإمسـاك    : <b>{result['results']['datetime'][0]['times']['Imsak']}</b>\
	            \n<b>شـروق الشمس  : <b>{result['results']['datetime'][0]['times']['Sunrise']}</b>\
	            \n<b>الـفجر     : <b>{result['results']['datetime'][0]['times']['Fajr']}</b>\
	            \n<b>الظـهر    : <b>{result['results']['datetime'][0]['times']['Dhuhr']}</b>\
	            \n<b>العـصر      : <b>{result['results']['datetime'][0]['times']['Asr']}</b>\
	            \n<b>غـروب الشمس   : <b>{result['results']['datetime'][0]['times']['Sunset']}</b>\
	            \n<b>المـغرب  : <b>{result['results']['datetime'][0]['times']['Maghrib']}</b>\
	            \n<b>العشـاء     : <b>{result['results']['datetime'][0]['times']['Isha']}</b>\
	            \n<b>منتـصف الليل : <b>{result['results']['datetime'][0]['times']['Midnight']}</b>\
		        \n\nᯓ 𝗦𝗢𝗨𝗥𝗖𝗘 𝗧𝗘𝗣𝗧𝗛𝗢𝗡╎@Tepthon\
	    "
	    await edit_or_reply(adzan, zedthonresult, "html")
    elif ZELZAL == "تونس":
	    url = f"http://api.aladhan.com/v1/timingsByCity?city=Tunis"
	    request = requests.get(url)
	    if request.status_code != 200:
	        await edit_delete(
	            adzan,
	            f"** لم يـتم العثور على هـذه المدينة {ZELZAL}**\n**-يرجى كتابة اسم العاصمـه او الدولـة بشكـل صحيـح** ",
	            5,
	        )
	        return
	    result = json.loads(request.text)
	    zedthonresult = f"<b>🕋╎أوقـات الصـلاة بالتـوقيت المحلـي لعواصـم الـدول <b>\
	            \n\n<b>المـدينة     : <b>تونـس</b>\
	            \n<b>الـدولة  : <b>تونـس</b>\
	            \n<b>التـاريخ     : <b>{result['results']['datetime'][0]['date']['gregorian']}</b>\
	            \n<b>الهـجري    : <b>{result['results']['datetime'][0]['date']['hijri']}</b>\
	            \n\n<b>الإمسـاك    : <b>{result['results']['datetime'][0]['times']['Imsak']}</b>\
	            \n<b>شـروق الشمس  : <b>{result['results']['datetime'][0]['times']['Sunrise']}</b>\
	            \n<b>الـفجر     : <b>{result['results']['datetime'][0]['times']['Fajr']}</b>\
	            \n<b>الظـهر    : <b>{result['results']['datetime'][0]['times']['Dhuhr']}</b>\
	            \n<b>العـصر      : <b>{result['results']['datetime'][0]['times']['Asr']}</b>\
	            \n<b>غـروب الشمس   : <b>{result['results']['datetime'][0]['times']['Sunset']}</b>\
	            \n<b>المـغرب  : <b>{result['results']['datetime'][0]['times']['Maghrib']}</b>\
	            \n<b>العشـاء     : <b>{result['results']['datetime'][0]['times']['Isha']}</b>\
	            \n<b>منتـصف الليل : <b>{result['results']['datetime'][0]['times']['Midnight']}</b>\
		        \n\nᯓ 𝗦𝗢𝗨𝗥𝗖𝗘 𝗧𝗘𝗣𝗧𝗛𝗢𝗡╎@Tepthon\
	    "
	    await edit_or_reply(adzan, zedthonresult, "html")
    elif ZELZAL == "ازمير" or ZELZAL == "اسطنبول" or ZELZAL == "انقره" or ZELZAL == "تركيا":
	    url = f"http://api.aladhan.com/v1/timingsByCity?city=Izmir"
	    request = requests.get(url)
	    if request.status_code != 200:
	        await edit_delete(
	            adzan,
	            f"** لم يـتم العثور على هـذه المدينة {ZELZAL}**\n**-يرجى كتابة اسم العاصمـه او الدولـة بشكـل صحيـح** ",
	            5,
	        )
	        return
	    result = json.loads(request.text)
	    zedthonresult = f"<b>🕋╎أوقـات الصـلاة بالتـوقيت المحلـي لعواصـم الـدول <b>\
	            \n\n<b>المـدينة     : <b>اسطنبـول</b>\
	            \n<b>الـدولة  : <b>تركيـا</b>\
	            \n<b>التـاريخ     : <b>{result['results']['datetime'][0]['date']['gregorian']}</b>\
	            \n<b>الهـجري    : <b>{result['results']['datetime'][0]['date']['hijri']}</b>\
	            \n\n<b>الإمسـاك    : <b>{result['results']['datetime'][0]['times']['Imsak']}</b>\
	            \n<b>شـروق الشمس  : <b>{result['results']['datetime'][0]['times']['Sunrise']}</b>\
	            \n<b>الـفجر     : <b>{result['results']['datetime'][0]['times']['Fajr']}</b>\
	            \n<b>الظـهر    : <b>{result['results']['datetime'][0]['times']['Dhuhr']}</b>\
	            \n<b>العـصر      : <b>{result['results']['datetime'][0]['times']['Asr']}</b>\
	            \n<b>غـروب الشمس   : <b>{result['results']['datetime'][0]['times']['Sunset']}</b>\
	            \n<b>المـغرب  : <b>{result['results']['datetime'][0]['times']['Maghrib']}</b>\
	            \n<b>العشـاء     : <b>{result['results']['datetime'][0]['times']['Isha']}</b>\
	            \n<b>منتـصف الليل : <b>{result['results']['datetime'][0]['times']['Midnight']}</b>\
		        \n\nᯓ 𝗦𝗢𝗨𝗥𝗖𝗘 𝗧𝗘𝗣𝗧𝗛𝗢𝗡╎@Tepthon\
	    "
	    await edit_or_reply(adzan, zedthonresult, "html")


