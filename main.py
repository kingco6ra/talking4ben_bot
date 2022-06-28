import os
import random

import telebot

token = os.environ.get('TOKEN')
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message: telebot.types.Message):
    voice = open('answer_sound/ben.mp3', 'rb')
    bot.send_voice(message.chat.id, voice)
    voice.close()
    bot.send_message(message.chat.id, "What's your question?")


@bot.message_handler(content_types=['text'])
def random_answer(message: telebot.types.Message):
    list_answers = ['yes', 'no', 'hihihi', 'hohoho']
    voice = open(f'answer_sound/{random.choice(list_answers)}.mp3', 'rb')
    bot.send_voice(message.chat.id, voice)
    voice.close()
    bot.send_message(234319155, f'{message.from_user.username}: {message.text}')


bot.infinity_polling()
