from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *
updater = Updater('5712451896:AAEwlba3PjwPpC0EXvaGYIJH8nDM-E2fNnM')
updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', summ_command))
updater.dispatcher.add_handler(CommandHandler('subt', subt_command))
updater.dispatcher.add_handler(CommandHandler('divi', divi_command))
updater.dispatcher.add_handler(CommandHandler('degr', degr_command))
updater.dispatcher.add_handler(CommandHandler('mult', mult_command))
print('Simple calc has been activated! use command */help* for read instruction')
updater.start_polling()
updater.idle()

