# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# CatTepthon #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Copyright (C) 2020-2023 by Tgzedub@Github.

# This file is part of: https://github.com/Tgzedub/catTepthon
# and is released under the "GNU v3.0 License Agreement".

# Please see: https://github.com/Tgzedub/catTepthon/blob/master/LICENSE
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Special credits: @amnd33p

import io
from datetime import datetime

import requests
from validators.url import url

from Tepthon import zedub

from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.google_tools import chromeDriver
from ..helpers.utils import reply_id

plugin_category = "utils"


@zedub.zed_cmd(
    pattern="(سكرين|gis)(?:\s|$)([\s\S]*)",
    command=("سكرين", plugin_category),
    info={
        "header": "لـ أخـذ نظرة للموقـع.",
        "usage": "{tr}ss <link>",
        "examples": "{tr}سكرين https://github.com/Tgzedub/catTepthon",
    },
)
async def screenshot(event):
    "To Take a screenshot of a website."
    cmd = event.pattern_match.group(1)
    text = event.pattern_match.group(2)
    reply = await event.get_reply_message()
    reply_to_id = await reply_id(event)
    if not text and reply:
        text = reply.text
    if not text:
        return await edit_delete(event, "أين رابط الموقع؟")
    if cmd == "ss":
        caturl = url(text)
        if not caturl:
            text = f"http://{text}"
            caturl = url(text)
        if not caturl:
            return await edit_delete(event, "⋙ هذا النوع من الروابط غير مدعوم")
    elif cmd == "gis":
        text = f"https://www.google.com/search?q={text}"
    catevent = await edit_or_reply(event, "`جـاري ...`")
    image, response = await chromeDriver.get_screenshot(text, catevent)
    if not image:
        return await edit_delete(catevent, response)

    await catevent.delete()
    with io.BytesIO(image) as out_file:
        out_file.name = f"{text}.PNG"
        await event.client.send_file(
            event.chat_id,
            out_file,
            caption=response,
            force_document=True,
            reply_to=reply_to_id,
            allow_cache=False,
            silent=True,
        )


@zedub.zed_cmd(
    pattern="scapture ([\s\S]*)",
    command=("scapture", plugin_category),
    info={
        "header": "To Take a screenshot of a website.",
        "description": "For functioning of this command you need to set SCREEN_SHOT_LAYER_ACCESS_KEY var",
        "usage": "{tr}scapture <link>",
        "examples": "{tr}scapture https://github.com/Tgzedub/catTepthon",
    },
)
async def scapture(event):
    "To Take a screenshot of a website."
    start = datetime.now()
    message_id = await reply_id(event)
    if Config.SCREEN_SHOT_LAYER_ACCESS_KEY is None:
        return await edit_or_reply(
            event,
            "`Need to get an API key from https://screenshotlayer.com/product and need to set it SCREEN_SHOT_LAYER_ACCESS_KEY !`",
        )
    catevent = await edit_or_reply(event, "`Processing ...`")
    sample_url = "https://api.screenshotlayer.com/api/capture?access_key={}&url={}&fullpage={}&viewport={}&format={}&force={}"
    input_str = event.pattern_match.group(1)
    inputstr = input_str
    caturl = url(inputstr)
    if not caturl:
        inputstr = f"http://{input_str}"
        caturl = url(inputstr)
    if not caturl:
        return await catevent.edit("`The given input is not supported url`")
    response_api = requests.get(
        sample_url.format(
            Config.SCREEN_SHOT_LAYER_ACCESS_KEY, inputstr, "1", "2560x1440", "PNG", "1"
        )
    )
    # https://stackoverflow.com/a/23718458/4723940
    contentType = response_api.headers["content-type"]
    end = datetime.now()
    ms = (end - start).seconds
    hmm = f"**url : **{input_str} \n**Time :** `{ms} seconds`"
    if "image" in contentType:
        with io.BytesIO(response_api.content) as screenshot_image:
            screenshot_image.name = "screencapture.png"
            try:
                await event.client.send_file(
                    event.chat_id,
                    screenshot_image,
                    caption=hmm,
                    force_document=True,
                    reply_to=message_id,
                )
                await catevent.delete()
            except Exception as e:
                await catevent.edit(str(e))
    else:
        await catevent.edit(f"`{response_api.text}`")
