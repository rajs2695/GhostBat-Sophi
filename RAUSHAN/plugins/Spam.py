from RAUSHAN import HANDLER
from RAUSHAN.__main__ import RAUSHAN
from config import OWNER_ID as OWN
from pyrogram import filters
import asyncio
import os

data = {}
@RAUSHAN.on_message(filters.command(['xspam', 'xsspam', 'xslspam', 'xdspam'], prefixes=HANDLER) & filters.me)
async def spam(_, message):
  global data
  m = message
  if m.command[0] == 'sspam':
    del data[m.chat.id]
    return await m.reply("Spam stopped.")
  elif data.get(m.chat.id):
    return await m.reply("There's an ongoing spam going on this chat, so yeah you can't use multipul spams.")
  if message.reply_to_message:
    r = message.reply_to_message
    data[m.chat.id] = True
    while data.get(message.chat.id):
      x = await r.copy(m.chat.id)
      if m.command[0] == 'slspam' or m.command[0] == 'dspam':
        await asyncio.sleep(2.5)
        if m.command[0] == 'dspam': await x.delete()
      else: await asyncio.sleep(0.7)
  else:
    if len(message.text.split()) < 2:
      return await m.reply("You should reply to a message or give a text input.")
    text = message.text.split(None, 1)[1]
    data[m.chat.id] = True
    while data.get(message.chat.id):
      x = await RAUSHAN.send_message(m.chat.id, text)
      if m.command[0] == 'slspam' or m.command[0] == 'dspam':
        await asyncio.sleep(2.5)
        if m.command[0] == 'dspam': await x.delete()
      else: await asyncio.sleep(0.7)

MOD_NAME = "Spam"
MOD_HELP = """.spam <text> - To spam the text or reply to a message to spam it.
.sspam - To stop the ongoing spam.
.slspam - Slow spam 2.5 sec delay for each.
.dspam - Same as slspam or (slow spam), but it delete's the spam message. used in chatfight rank boosting.
"""