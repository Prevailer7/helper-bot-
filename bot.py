import telebot

TOKEN = "8707508404:AAF1cI6ogosWqQh_egkeDtYf3a3M1slCNWM"  # <-- Change am to your token from BotFather

bot = telebot.TeleBot(TOKEN)

answers = {
    "wetin be your name": "My name na Helper Bot, your personal assistant 🤖",
    "what is your name": "My name na Helper Bot, your personal assistant 🤖",
    "who be your name": "My name na Helper Bot, your personal assistant 🤖",
    "wetin you sabi do": "I sabi answer question, tell joke, and repeat wetin you talk. Type /help for more.",
    "what can you do": "I sabi answer question, tell joke, and repeat wetin you talk. Type /help for more.",
    "how you dey": "I dey fine o! Thank you say you ask. How you dey?",
    "how are you": "I dey fine o! Thank you say you ask. How you dey?",
    "who make you": "Na Max Chike make me! Na my oga be that 💪",
    "who created you": "Na Max Chike make me! Na my oga be that 💪",
    "wetin be render": "Render na where I dey live for internet. Na here Max put me make I no sleep.",
    "what is render": "Render na where I dey live for internet. Na here Max put me make I no sleep.",
    "joke": "Why programmer no like sunlight? Because e get too many bugs! 😂",
    "tell me joke": "Why programmer no like sunlight? Because e get too many bugs! 😂",
    "help": "I sabi answer these questions:\n\n- wetin be your name\n- wetin you sabi do\n- how you dey\n- who make you\n- wetin be render\n- joke\n\nTry am!",
    "hi": "Hello Max! 👋 Wetin you want make I do for you today?",
    "hello": "Hello Max! 👋 Wetin you want make I do for you today?",
    "ok": "Ok my oga! Wetin next?",
    "correct": "Correct! You sabi book o 😎",
    "thank you": "You be welcome! Na my work be that.",
    "thanks": "You be welcome! Na my work be that.",
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"Hello {message.from_user.first_name}! 👋\nNa me be your Helper Bot.\nAsk me question, or type /help make you see wetin I sabi do.")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, answers["help"])

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    text = message.text.lower().strip()
    
    # Remove ? and .
    text = text.replace("?", "").replace(".", "")
    
    if text in answers:
        bot.reply_to(message, answers[text])
    else:
        bot.reply_to(message, f"You talk say: '{message.text}'\n\nTry /help, I sabi more things now!")

print("Bot don start...")
bot.infinity_polling()