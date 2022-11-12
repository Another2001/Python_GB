from html_creater import createhtml
from telegram import Update
from telegram.ext import Updater, Filters, CommandHandler, MessageHandler, CallbackContext
from bot_commands import *
createhtml()

updater = Updater('5712451896:AAEwlba3PjwPpC0EXvaGYIJH8nDM-E2fNnM')

updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('add', add_com))
updater.dispatcher.add_handler(CommandHandler('show_all', view_com))
updater.dispatcher.add_handler(CommandHandler('show', view_com_select))
updater.dispatcher.add_handler(CommandHandler('delete', delete_command))

updater.start_polling()
updater.idle()
