from webbrowser import open_new
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from spy_log import *
import IO_json

operation = 0
operands = []
path = f"NineHW/task1/db.json"


def help_command(update: Update, context: CallbackContext):
    global operation 
    operation = 0

    res_str = ""
    res_str += "ТЕЛЕФОННЫЙ СПРАВОЧНИК\n"
    res_str += "Выберите одно из доступных действий :\n"
    res_str += "Добавить запись /add\n"
    res_str += "Показать записи /show_all\n"
    res_str += "Показать запись(выборка) /show\n"
    res_str += "Удалить запись(выборка) /delete\n"
    update.message.reply_text(res_str)


def add_com(update: Update, context: CallbackContext):
    msg = update.message.text.split(" ")
    if len(msg) == 3:
        if len(msg[1])!=0 and len(msg[2])!=0:
            IO_json.append_to_json(path,msg[1:])
            update.message.reply_text(f"Добавлена запись {msg[1]} {msg[2]}\n")
            log()
            return
    update.message.reply_text("Введены неправильные данные")

def view_com(update: Update, context: CallbackContext):
    db_list = IO_json.read_all_from_json(path)
    update.message.reply_text(db_list)
    log()

def view_com_select(update: Update, context: CallbackContext):
    update.message.reply_text(f"Введите какую-либо информацию искомого человека: ")
    msg = update.message.text.split(" ")
    db_list = IO_json.read_from_json(path)
    for i in db_list:
        if msg[1] or msg[2] in db_list:
            update.message.reply_text(i)
    log()

def delete_command(update: Update, context: CallbackContext):
    update.message.reply_text(f"Кого удаляем? :")
    db_list = update.message.text.split(" ")
    db_list = IO_json.delete_from_json(path)
    update.message.reply_text(db_list)
    log()
