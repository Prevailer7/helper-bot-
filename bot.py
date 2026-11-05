import os
import random

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")

JOKES = [
    "Why computer no dey hungry? Because e get plenty bytes! 😂",
    "Teacher: Why you late? Pikin: Sir, signboard talk say 'School Ahead, Go Slow' 😂",
    "Wetin be difference between your bot and NEPA? My bot dey respond sharp sharp! 😂",
    "Why student carry ladder go school? Because e hear say high level dey inside 😂",
    "I no be robot, I be your helper wey sabi joke small-small 😎"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.effective_user.first_name
    await update.message.reply_text(
        f"Hello {name}! 👋\n"
        "Na me be your Helper Bot.\n"
        "Ask me question, or type /help make you see wetin I sabi do."
    )

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Wetin I sabi do:\n"
        "/start - Welcome message\n"
        "/help - Show this list\n"
        "/joke - I go tell you joke\n\n"
        "Ask me question like:\n"
        "- Wetin be your name?\n"
        "- How you dey?\n"
        "- Who make you?\n"
        "- What can you do?\n\n"
        "If na question wey I no sabi, I go repeat am."
    )

async def joke_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(JOKES))

async def answer_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower().strip()

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
        reply = f"Good question! You ask: '{update.message.text}'\nI still dey learn, but I go try answer you soon. For now, try ask me 'How you dey?'"
    else:
        reply = f"You talk say: '{update.message.text}'\n\nTry /help, I sabi more things now!"

    await update.message.reply_text(reply)

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("joke", joke_cmd))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, answer_question))

    print("Bot don start...")
    app.run_polling()

if __name__ == "__main__":
    main()