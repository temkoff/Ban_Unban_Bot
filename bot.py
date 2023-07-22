import telebot
import config
import keyboard
bot = telebot.TeleBot(config.TOKEN)
admin_id = 413632589  # ID АДМИННИСТРАТОРА
list_group_id = []
list_group_https = []


# СООБЩЕНИЕ В ЧАТЕ ГРУППЫ
@bot.message_handler(commands=['start'], chat_types=['group', 'supergroup'])
def welcome(message):
    if message.from_user.id == admin_id:
        list_group_id.append(message.chat.id)
        bot.send_message(message.chat.id, 'Привет! Теперь я буду банить!')
        https = bot.export_chat_invite_link(message.chat.id)
        list_group_https.append(https)


# СООБЩЕНИЕ В ПЕРЕПИСКЕ С БОТОМ
@bot.message_handler(commands=['start'], chat_types=['private'])
def welcome(message):
    if message.from_user.id == admin_id:
        keyboard.home(message)
    else:
        bot.send_message(message.chat.id, 'Я не буду выполянть ваши команды.')


# ОБРАБОТЧИК МЕНЮ
@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == 'list':
        spisok(call.message)
    elif call.data == 'ban':
        keyboard.ban(call.message)
    elif call.data == 'unban':
        keyboard.unban(call.message)
    elif call.data == 'ban_all':
        _id_ = bot.reply_to(call.message, "Напишите id для бана")
        bot.register_next_step_handler(_id_, ban)
    elif call.data == 'unban_all':
        _id_ = bot.reply_to(call.message, "Напишите id для разбана")
        bot.register_next_step_handler(_id_, unban)
    elif call.data == 'ban_vib':
        _id_ = bot.reply_to(call.message, "Напишите номер группы(номер можно посмотреть в списке)")
        bot.register_next_step_handler(_id_,ban_vib)
    elif call.data == 'unban_vib':
        _id_ = bot.reply_to(call.message, "Напишите номер группы(номер можно посмотреть в списке)")
        bot.register_next_step_handler(_id_,unban_vib)
    elif call.data == 'glav':
        keyboard.home(call.message)
    else:
        bot.send_message(call.message.chat.id, 'Пишите коректно')


@bot.message_handler(content_types=['text'], chat_types=['private'])
def spisok(message):
    dict_group = dict(zip(list_group_https, list_group_id))
    print(dict_group.items())
    i = 0
    while i < len(dict_group.items()):
        for key, value in dict_group.items():
            bot.send_message(message.chat.id, "{0}){1}: {2}".format(i, key, value))
            i += 1


# БАН
def ban(message):
    message_to_save = message.text
    for i in range(len(list_group_id)):
        bot.ban_chat_member(chat_id=list_group_id[i], user_id=message_to_save)


def ban_vib(message):
    dict_group = dict(zip(list_group_https, list_group_id))
    print(list(dict_group.items()))
    message_to_save = message.text
    i = 0
    while i < len(dict_group.items()):
        if message_to_save == i:
            bot.reply_to(message, "ID для бана")
            message_to_save_2 = message.text
            bot.ban_chat_member(chat_id=list_group_id[i], user_id=message_to_save_2)
            i += 1


# РАЗБАН
def unban(message):
    message_to_save = message.text
    for i in range(len(list_group_id)):
        bot.unban_chat_member(chat_id=list_group_id[i], user_id=message_to_save)


def unban_vib(message):
    dict_group = dict(zip(list_group_https, list_group_id))
    print(list(dict_group.items()))
    message_to_save = message.text
    i = 0
    while i < len(dict_group.items()):
        if message_to_save == i:
            bot.reply_to(message, "ID для разбана")
            message_to_save_2 = message.text
            bot.unban_chat_member(chat_id=list_group_id[i], user_id=message_to_save_2)
            i += 1


bot.polling(none_stop=True)
