from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from spy import *


def hi_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Hi {update.effective_user.first_name}!')


def help_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'/hi\n/time\n/help\n/summ\n/subt\n/divi\n/degr')


def time_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'{datetime.datetime.now().time()}')


def summ_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()  # сумма элементов через пробел  (1)_+_(2)
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} + {y} = {x + y}')


def subt_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()  # разница элементов через пробел  (1)_-_(2)
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} - {y} = {x - y}')


def divi_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()  # отношение элементов через пробел  (1)_/_(2)
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} / {y} = {x / y}')


def degr_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()  # степень элемента (1) в значении (2) через пробел  (1)_**_(2)
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} in degree {y} = {x ** y}')


def mult_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()  # произведение элементов через пробел  (1)_*_(2)
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} * {y} = {x * y}')
