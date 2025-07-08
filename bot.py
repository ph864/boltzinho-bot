import os
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Obtenha o token do ambiente
TOKEN = os.getenv("TELEGRAM_TOKEN")

def start(update, context):
    update.message.reply_text("Fala meu chapa, aqui é o Boltzinho! 🤖")

def respond(update, context):
    user_msg = update.message.text.lower()
    if "gemini" in user_msg:
        update.message.reply_text("Pau no rabo do Gemini kkkkk 🤣")
    elif "açaí" in user_msg:
        update.message.reply_text("Já pagou o açaí da Wictoria, seu safado? 😂")
    else:
        update.message.reply_text("Tô aqui, manda a braba! 🔥")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, respond))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
