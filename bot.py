import telebot
import random
from datetime import datetime

TOKEN = "8707508404:AAF1cI6ogosWqQh_egkeDtYf3a3M1slCNWM"

bot = telebot.TeleBot(TOKEN)

jokes = [
    "Why did the danfo driver cross the road? To avoid LASTMA! 😂",
    "Lagos traffic no be joke, but we still dey smile!",
    "NEPA take light? No worry, your bot still get power! ⚡"
]

lagos_tips = [
    "Traffic tip: Avoid 3rd Mainland Bridge 7-10am & 4-8pm if you can!",
    "Danfo tip: Always ask 'Owo da?' before you enter!",
    "Lagos hack: Use BRT lane if you get BRT, but no follow yellow bus lane o!",
    "If you dey Oshodi, hold your phone tight! 😅"
]

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🚀 Welcome back boss! Lagos Helper Bot is FULLY AWAKE!\n\nType /help to see wetin I fit do.")

@bot.message_handler(commands=['help'])
def help_cmd(message):
    bot.reply_to(message, "🤖 *What I fit do for you:*\n/start - Wake me up\n/help - See this list\n/lagos - Get Lagos traffic tips\n/joke - I go crack Naija joke\n/time - Current time\n\nJust send any message and I go reply!", parse_mode="Markdown")

@bot.message_handler(commands=['lagos'])
def lagos_cmd(message):
    tip = random.choice(lagos_tips)
    bot.reply_to(message, f"📍 Lagos Tip:\n{tip}")

@bot.message_handler(commands=['joke'])
def joke_cmd(message):
    joke = random.choice(jokes)
    bot.reply_to(message, f"😂 {joke}")

@bot.message_handler(commands=['time'])
def time_cmd(message):
    now = datetime.now().strftime("%I:%M %p")
    bot.reply_to(message, f"⏰ Time now na {now} for Lagos!")

@bot.message_handler(func=lambda m: True)
def all_messages(message):
    bot.reply_to(message, f"You talk say: '{message.text}'\n\nTry /help, I sabi more things now!")

print("✅ Lagos Helper Bot Level 2 is running...")
bot.infinity_polling()
