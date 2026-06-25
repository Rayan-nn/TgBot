import re
import sys
import os
import telebot
from telebot import types
from texts import *
from telebot.types import InputMediaPhoto

DEBUG = "--debug" in sys.argv
if DEBUG:
    print("Режим откладки включён")


bot = telebot.TeleBot(os.getenv('8851650718:AAH7LYAN-YFBRXY4gW-34KyOaL1FYLemPm8'))



def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.row("👤 О себе", "🎯 Моя цель")
    markup.row("💻 IT история", "👩‍🏫 Мой ментор")
    markup.row("📈 Прогресс", "🎮 Хобби")
    markup.row("🏆 Работы", "🔗 GitHub")
    markup.row("📚 Help")

    return markup



@bot.message_handler(commands=['start'])
def start(message):
    welcome = """
    👋 Добро пожаловать в моё интерактивное портфолио!

    Меня зовут Райиан, я начинающий разработчик Python и участник школы программирования CAP Education.

    Этот бот расскажет обо мне, моём пути IT, целях, доситижениях и лучших проектах.

    📌 Выберите интересующий раздел в меню ниже и познакомтесь со мной поближе.

    🚀 Начните знакомство с моим портфолио, выбрав один из разделов ниже. Для получения списка всех команд используйте /help.
    """
    bot.send_message(message.chat.id, welcome, reply_markup=main_menu())



@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, HELP, parse_mode='Markdown')



@bot.message_handler(commands=['about'])
def about(message):
    bot.send_message(message.chat.id, ABOUT, parse_mode='Markdown')



@bot.message_handler(commands=['goal'])
def goal(message):
    bot.send_message(message.chat.id, GOAL, parse_mode='Markdown')



@bot.message_handler(commands=['itstory'])
def itstory(message):
    bot.send_message(message.chat.id, ITSTORY, parse_mode='Markdown')



@bot.message_handler(commands=['mentor'])
def mentor(message):
    bot.send_message(message.chat.id, MENTOR, parse_mode='Markdown')



@bot.message_handler(commands=['progress'])
def progress(message):
    bot.send_message(message.chat.id, PROGRESS, parse_mode='Markdown')



@bot.message_handler(commands=['hobby'])
def hobby(message):
    bot.send_message(message.chat.id, HOBBY, parse_mode='Markdown')



@bot.message_handler(commands=['works'])
def works(message):

    try:
        bot.send_message(message.chat.id, WORK1, parse_mode='Markdown')

        media1 = [
            InputMediaPhoto(open("screenshots/work1_1.png", "rb")),
            InputMediaPhoto(open("screenshots/work1_2.png", "rb")),
            InputMediaPhoto(open("screenshots/work1_3.png", "rb")),
            InputMediaPhoto(open("screenshots/work1_4.png", "rb")),
        ]

        bot.send_media_group(message.chat.id, media1)


        bot.send_message(message.chat.id, WORK2, parse_mode='Markdown')

        media2 = [
            InputMediaPhoto(open("screenshots/work2_1.png", "rb")),
            InputMediaPhoto(open("screenshots/work2_2.png", "rb")),
            InputMediaPhoto(open("screenshots/work2_3.png", "rb")),
        ]

        bot.send_media_group(message.chat.id, media2)

        bot.send_message(message.chat.id, "⬇️ Меню", reply_markup=main_menu())
    except Exception as e:
        bot.send_message(
            message.chat.id,
            "Ошибка загрузки работ"
        )



@bot.message_handler(commands=['github'])
def github(message):
    bot.send_message(message.chat.id, GITHUB, parse_mode='Markdown')



@bot.message_handler(commands=['check_email'])
def check_email(message):
    bot.send_message(
        message.chat.id,
        "Отправьте email для проверки")



@bot.message_handler(content_types=['text'])
def handle_text(message):

    if message.text == "👤 О себе":
        bot.send_message(message.chat.id,  ABOUT, parse_mode='Markdown', reply_markup=main_menu())

    elif message.text == "🎯 Моя цель":
        bot.send_message(message.chat.id,  GOAL, parse_mode='Markdown', reply_markup=main_menu())
        
    elif message.text == "💻 IT история":
        bot.send_message(message.chat.id,  ITSTORY, parse_mode='Markdown', reply_markup=main_menu())
    
    elif message.text == "👩‍🏫 Мой ментор":
        bot.send_message(message.chat.id,  MENTOR, parse_mode='Markdown', reply_markup=main_menu())
    
    elif message.text == "📈 Прогресс":
        bot.send_message(message.chat.id,  PROGRESS, parse_mode='Markdown', reply_markup=main_menu())
    
    elif message.text == "🎮 Хобби":
        bot.send_message(message.chat.id,  HOBBY, parse_mode='Markdown', reply_markup=main_menu())
    
    elif message.text == "🏆 Работы":
        works(message)

    elif message.text == "🔗 GitHub":
        bot.send_message(message.chat.id,  GITHUB, parse_mode='Markdown', reply_markup=main_menu())

    elif message.text == "📚 Help":
        bot.send_message(message.chat.id,  HELP, parse_mode='Markdown', reply_markup=main_menu())

    elif "@" in message.text:

        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        
        if re.match(pattern, message.text):
            bot.send_message(
                message.chat.id,
                "✅ Email введен корректно. "
            )
        else:
            bot.send_message(
                message.chat.id,
                "❌ Неверный формат email."
            ) 

    else:
        bot.send_message(
            message.chat.id,
            "Выберите раздел с помощью кнопок меню или используйте /help.",
            reply_markup=main_menu()
        )


if __name__ == "__main__":
    bot.infinity_polling()

