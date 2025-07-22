# main.py - Raptor Bot (XAUUSD - SMC Logic)

from telegram import Bot
import os

TOKEN = os.getenv("BOT_TOKEN")
USER_ID = os.getenv("USER_ID")

def send_signal(message):
    bot = Bot(token=TOKEN)
    bot.send_message(chat_id=USER_ID, text=message)

# Placeholder: semnal generat când toate condițiile SMC sunt îndeplinite
send_signal("📈 Signal XAUUSD: MSS + Liquidity Grab + FVG ✅")
