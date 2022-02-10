from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

from config import TOKEN

from main import parse, get_content

def hello(update: Update, context: CallbackContext) -> None:
    r = parse()
    for i in r:
        update.message.reply_text(f'{i}')


updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('start', hello))

updater.start_polling()
updater.idle()