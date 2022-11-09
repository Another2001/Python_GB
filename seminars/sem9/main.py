from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *

updater = Updater('5457327978:AAElZlvnGDyuL2kzxyOn-Dc849ow34LxPlI')

updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))
updater.dispatcher.add_handler(CommandHandler('w_d', w_d_command))
updater.dispatcher.add_handler(CommandHandler('ran', ran_command))

updater.start_polling()
updater.idle()
