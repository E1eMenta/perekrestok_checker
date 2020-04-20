import datetime
import time

import telebot

from perekrestok_check import check

CONTINUE = True

if __name__ == '__main__':
    TOKEN = 'Токкен'
    bot = telebot.TeleBot(TOKEN)


    @bot.message_handler(commands=['start'])
    def start_message(message):
        while True:
            try:
                result = check()
            except Exception as inst:
                bot.send_message(message.chat.id, f'Какая-то ошибка {type(inst)}')
                result = False

            print(f"{result}. Time: {datetime.datetime.now()}")
            if result:
                bot.send_message(message.chat.id, f'Появилось время {datetime.datetime.now()}')

            time.sleep(15 * 60)
            while True:
                if CONTINUE:
                    break
                else:
                    time.sleep(60)


    @bot.message_handler(content_types=['text'])
    def send_text(message):
        global CONTINUE
        if message.text.lower() == 'stop':
            CONTINUE = False
            bot.send_message(message.chat.id, f'Sir, yes, sir. Stop thinking')
        elif message.text.lower() == 'start':
            CONTINUE = True
            bot.send_message(message.chat.id, f'Sir, yes, sir. Continue thinking')


    bot.polling()
