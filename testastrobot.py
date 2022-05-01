import telebot

token ='*****'

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def echo(message):
    name = 'Саша'
    name1 = 'Маша'
    if name in message.text:
        bot.send_message(message.chat.id, "Ба! Знакомые все лица!")
    elif name1 in message.text:
        bot.send_message(message.chat.id, "Ну что, забуримся в астрал?")
    else:
        bot.send_message(message.chat.id, message.text)

bot.polling(non_stop=True)
