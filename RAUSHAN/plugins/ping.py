from RAUSHAN import *
from RAUSHAN.__main__ import RAUSHAN as bot
from config import OWNER_ID
from config import SUDO_USERS_ID
from pyrogram import filters
from pyrogram import *
import asyncio
import os
import requests
from datetime import datetime
import time

def ping_website(url):
    try:
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()

        if response.status_code == 200:
            response_time_ms = (end_time - start_time) * 1000
            return f"{response_time_ms:.2f}ms"
        else:
            return f"Failed to ping {url}. Status code: {response.status_code}"

    except requests.ConnectionError:
        return f"» Failed to connect to {url}"

telegram_url = "https://google.com"

@bot.on_message(filters.command("xping", prefixes=HANDLER) & filters.user('me'))
async def ping_pong(client, message):
    start_time = bot_start_time
    end_time = datetime.now()
    ping_time = (end_time - start_time).total_seconds() * 1000
    uptime = (end_time - bot_start_time).total_seconds()
    hours, remainder = divmod(uptime, 3600)
    minutes, seconds = divmod(remainder, 60)
    await message.reply_text(f"» Pᴏɴɢ! Rᴇsᴘᴏɴsᴇ ᴛɪᴍᴇ: {ping_website(telegram_url)}\n» Uᴘᴛɪᴍᴇ: {int(hours)}h {int(minutes)}m {int(seconds)}s")
