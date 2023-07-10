import telebot
from reqest import rusInfo
token = '5622740231:AAHAFtpX1vBnrKryyn9-ycptyYG6zZrGlr8'
bot = telebot.TeleBot(token)

@bot.message_handler(commands = ['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет. Мне нужна ссылка на вк")

@bot.message_handler(content_types = ['text'])
def stat_message_handler(message):
    text = message.text
    chat_id = message.chat.id
    inf = rusInfo(text)
    print(000000)
    if inf in (201, 401):
        bot.send_message(chat_id, 'неверная ссылка')
    else:
        bot.send_message(chat_id, f'Xозяин этой страницы {inf[0]} {inf[1]}')

bot.infinity_polling()

