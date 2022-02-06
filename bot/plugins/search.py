#    This file is part of the Forwarder distribution.
#    Copyright (c) 2022 kaif-00z
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in
# <https://github.com/kaif-00z/ForwarderBot/blob/main/License> .


from . import *
from .dbs.ban_db import is_ban

Z = []
X = []
A = []
B = []

@bot.on(
    events.NewMessage(incoming=True, pattern="\\/search", func=lambda e: e.is_private)
)
async def search(event):
    if is_ban(event.sender_id):
        return await event.reply(
            "You are Banned contact the Admin of the Bot for Unban"
        )
    query = ""
    try:
        query = event.text.split(" ", maxsplit=1)[1]
    except BaseException:
        pass
    if not query:
        return await event.reply("`Plz gib some query to search`")
    btn = [Button.inline("CANCEL PROCESS", data="cnc")]
    x = await event.reply("`searching...`", buttons=btn)
    async for message in user.iter_messages(Var.GROUP_ID, search=query):
        if message:
            if event.sender_id not in X:
                X.append(event.sender_id)
            msg = await bot.get_messages(Var.GROUP_ID, ids=message.id)
            await bot.send_message(event.chat_id, msg)
            if event.sender_id in Z:
                Z.remove(event.sender_id)
                return await x.delete()
            await asyncio.sleep(1.5)
            continue
    if event.sender_id not in X:
        await bot.send_message(
            event.chat_id,
            f"**Nothing Found Related To Keyword :** `{query}`",
        )
    else:
        await bot.send_message(
            event.chat_id,
            f"**All Files Related To Keyword :** `{query}` **sent successfully.**",
        )
        X.remove(event.sender_id)
    await x.delete()


@bot.on(events.callbackquery.CallbackQuery(data=re.compile("cnc")))
async def _(event):
    Z.append(event.sender_id)
#--------------------&&&----------


@bot.on(
    events.NewMessage(incoming=True, pattern="\\/moviesearch", func=lambda e: e.is_private)
)
async def search(event):
    if is_ban(event.sender_id):
        return await event.reply(
            "You are Banned contact the Admin of the Bot for Unban"
        )
    query = ""
    try:
        query = event.text.split(" ", maxsplit=1)[1]
    except BaseException:
        pass
    if not query:
        return await event.reply("`Plz gib some query to search`")
    btn = [Button.inline("CANCEL PROCESS", data="c_nc")]
    x = await event.reply("`searching...`", buttons=btn)
    async for message in user.iter_messages(Var.GROUP_ID2, search=query):
        if message:
            if event.sender_id not in A:
                A.append(event.sender_id)
            msg = await bot.get_messages(Var.GROUP_ID2, ids=message.id)
            await bot.send_message(event.chat_id, msg)
            if event.sender_id in B:
                B.remove(event.sender_id)
                return await x.delete()
            await asyncio.sleep(1.5)
            continue
    if event.sender_id not in A:
        await bot.send_message(
            event.chat_id,
            f"**Nothing Found Related To Keyword :** `{query}`\n**",
        )
    else:
        await bot.send_message(
            event.chat_id,
            f"**All Files Related To Keyword :** `{query}` **sent successfully.**",
        )
        A.remove(event.sender_id)
    await x.delete()


@bot.on(events.callbackquery.CallbackQuery(data=re.compile("c_nc")))
async def _(event):
    B.append(event.sender_id)
