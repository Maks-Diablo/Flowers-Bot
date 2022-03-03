import requests
from datetime import *
import telebot
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from telebot import types


def day_time():    #Определяем вид дня
    global day_hours
    now = datetime.now()
    day_hours = now.strftime("%H")
    if (day_hours >= "22"):
        day_hours = "Доброй ночи,"
    elif(day_hours < "07"):
        day_hours = "Доброй ночи,"
    elif (day_hours >= "07") and (day_hours < "12"):
        day_hours = "Доброе утро,"
    elif (day_hours >= "12") and (day_hours < "18"):
        day_hours = "Добрый день,"
    elif (day_hours >= "18") and (day_hours < "22"):
        day_hours = "Добрый вечер,"
    return day_hours
def telegram_bot():
    bot = telebot.TeleBot('5205670895:AAFlbuNp91KUl0jO52rPBEpCkQcQl2yoQG0')


    @bot.message_handler(commands=["start"])
    def start_message(message):

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Да")
        markup.add(btn1)
        day_time()
        bot.send_message(message.chat.id, text=f"{day_hours}" + "{0.first_name}!\nВас приветствует Бот цветочного "
                                                                "магазина \"Название магазина\"\nХотите посмотреть наш "
                                                                "ассортимент?".format(message.from_user),
                         reply_markup=markup)

    @bot.message_handler(content_types=["text"])
    def send_text(message):
        if message.text.lower() == "да":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
            btn1 = types.KeyboardButton("Готовые букеты")
            btn2 = types.KeyboardButton("Собрать свой")
            markup.add(btn1,btn2)
            day_time()
            bot.send_message(message.chat.id, text='Хорошо! Хотите посмотреть готовые букеты или собрать свой?'\
                             .format(message.from_user),reply_markup=markup)

        elif message.text.lower() == "готовые букеты":
            bot.send_message(message.chat.id, text='"тут скинулись готовые букеты"'.format())
        elif message.text.lower() == "собрать свой":
            bot.send_message(message.chat.id, text='"а тут я хз"'.format())
        else:
            bot.send_message(message.chat.id, 'Ошибка!')

    bot.polling()

if __name__ == '__main__':
    telegram_bot()
