import os
import random
import telebot

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

JOKES = [
    "Why computer no dey hungry? Because e get plenty bytes! 😂",
    "Teacher: Why you late? Pikin: Sir, signboard talk say 'School Ahead, Go Slow' 😂",
    "Wetin be difference between your bot and NEPA? My bot dey respond sharp sharp! 😂",
    "Why student carry ladder go school? Because e hear say high level dey inside 😂",
    "I no be robot, I be your helper wey sabi joke small-small 😎"
]

@bot.message_handler(commands=['start'])
def start(message):
    name = message.from_user.first_name
    bot.reply_to(message, f"Hello {name}! 👋\nNa me be your Helper Bot.\nAsk me question, or type /help make you see wetin I sabi do.")

@bot.message_handler(commands=['help'])
def help_cmd(message):
    bot.reply_to(message, "Wetin I sabi do:\n/start - Welcome message\n/help - Show this list\n/joke - I go tell you joke\n\nAsk me question like:\n- Wetin be your name?\n- How you dey?\n- Who make you?\n- What can you do?")

@bot.message_handler(commands=['joke'])
def joke_cmd(message):
    bot.reply_to(message, random.choice(JOKES))

@bot.message_handler(func=lambda m: True)
def answer_question(message):
    text = message.text.lower().strip()

    if "your name" in text:
        reply = "My name na Helper Bot, your personal assistant 🤖"
    elif "how you dey" in text or "how are you" in text:
        reply = "I dey fine o! Thanks for asking. How you dey too? 😊"
    elif "who make you" in text or "who created you" in text or "who be your oga" in text:
        reply = "Na Max Chike be my oga! Na im build me for Render 😎"
    elif "what can you do" in text or "wetin you sabi do" in text:
        reply = "I sabi answer question, tell joke, and repeat wetin you talk. Type /help for more."
    elif "thank" in text:
        reply = "You are welcome! Na my work be that 🙏"
    elif "bye" in text or "goodbye" in text:
        reply = "Bye bye! Come back anytime you need help 👋"
    elif text.endswith("?"):
        reply = f"Good question! You ask: '{message.text}'\nI still dey learn, but I go try answer you soon. For now, try ask me 'How you dey?'"
    else:
        reply = f"You talk say: '{message.text}'\n\nTry /help, I sabi more things now!"

    bot.reply_to(message, reply)

print("Bot don start...")
bot.polling()