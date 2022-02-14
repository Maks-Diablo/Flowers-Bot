import requests
from datetime import *
import telebot
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from telebot import types


def telegram_bot():
    bot = telebot.TeleBot('5205670895:AAFlbuNp91KUl0jO52rPBEpCkQcQl2yoQG0')
#Определяем вид дня
    now = datetime.now()
    day_hours = now.strftime("%H")
    if (day_hours > "22") and (day_hours < "7"):
        day_hours = "Доброй ночи!"
    elif (day_hours > "7") and (day_hours < "12"):
        day_hours = "Доброе утро!"
    elif (day_hours > "12") and (day_hours < "18"):
        day_hours = "Добрый день!"
    elif (day_hours > "18") and (day_hours < "22"):
        day_hours = "Добрый вечер!"

    @bot.message_handler(commands=["start"])
    def start_message(message):
        #bot.send_message(message.chat.id, f'{day_hours}\nВас приветствует Бот цветочного магазина "Название магазина"\nХотите посмотреть наш ассортимент?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👋 Поздороваться")
        btn2 = types.KeyboardButton("❓ Задать вопрос")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id,
                         text="Привет, {0.first_name}! Я тестовый бот для твоей статьи для habr.com".format(
                             message.from_user), reply_markup=markup)

    @bot.message_handler(content_types=["text"])
    def send_text(message):
        if message.text.lower() == "да":

            bot.send_message(
                message.chat.id,
                "Круто"
            )

        else:
            bot.send_message(message.chat.id, 'Придура... Напиши "Го"')

    bot.polling()

if __name__ == '__main__':
    telegram_bot()
