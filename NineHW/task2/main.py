from telegram import Update
from telegram.ext import Updater, Filters, CommandHandler, MessageHandler, CallbackContext
from bot_commands import *

updater = Updater('5712451896:AAEwlba3PjwPpC0EXvaGYIJH8nDM-E2fNnM')

updater.dispatcher.add_handler(CommandHandler('start', start_command))
updater.dispatcher.add_handler(CommandHandler('exit', quit_command))

updater.dispatcher.add_handler(MessageHandler(Filters.text, analize_command))

updater.start_polling()
updater.idle()
