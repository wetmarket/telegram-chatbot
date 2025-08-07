from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv
import os

load_dotenv()

def start(update, context):
    update.message.reply_text("Hello, World!")

def main():
    updater = Updater(os.getenv('TOKEN'), use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()