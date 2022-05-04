import telebot
import random

token = '*****'

bot = telebot.TeleBot(token)

HELP = """
/help - вывести справку по программе
/add - добавить новую задачу [формат ввода: </add> <пробел> <дата(yyyy-mm-dd)> <пробел> <описание задачи>]; минимальная длина новой задачи - 5 символов
/show - вывести список задач на указанную дату [формат ввода: <yyyy-mm-dd> или <Сегодня>]
/random - добавить случайную задачу на сегодня
"""
RANDOM_TASKS = ["Погулять", "Сделать упражнения", "Поиграть с сыном", "Заняться сексом с женой", "Выспаться"]
tasks = {}

def add_new(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=["add"])
def add(message):
    command = message.text.split(maxsplit=2)
    if len(command)<3:
        text = "формат ввода: </add> <пробел> <дата(yyyy-mm-dd)> <пробел> <описание задачи>"
    else:
        date = command[1]
        task = command[2]
        if len(task)<5:
            text = "Минимальная длина новой задачи - 5 символов"
        else:
            add_new(date, task)
            text = "Задача " + "'" + task + "'" + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["random"])
def random_add(message):
    date = "Сегодня"
    # на строчке выше нужен код автоматической подстановки сегодняшней даты, а не это
    task = random.choice(RANDOM_TASKS)
    add_new(date, task)
    text = "Задача " + "'" + task + "'" + " добавлена на дату Сегодня"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["show", "print"])
def show(message):
    command = message.text.split(maxsplit=1)
    date = command[1]
    text = ""
    if date in tasks:
        text = date + "\n"
        for task in tasks[date]:
            text = text + ">>  " + task + "\n"
    else:
        text = "Нет задач на указанную дату"
    bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)
