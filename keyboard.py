import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(content_types=['text'])
# Первая клавиатура при запуске(приветстиве)
def Home(message):
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='СПИСОК ГРУПП', callback_data='list')
    item2 = types.InlineKeyboardButton(text='БАН', callback_data='ban')
    item3 = types.InlineKeyboardButton(text='РАЗБАН', callback_data='unban')

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, ' Привет, {0.first_name}, выберите один из пункотов.'.format(message.from_user), reply_markup=markup)


# Клавиатура полсе кнопки 'ГЛАВНАЯ'
def home(message):
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='СПИСОК ГРУПП', callback_data='list')
    item2 = types.InlineKeyboardButton(text='БАН', callback_data='ban')
    item3 = types.InlineKeyboardButton(text='РАЗБАН', callback_data='unban')

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, '{0.first_name}, выберите один из пункотов.'.format(message.from_user), reply_markup=markup)


# Клавиатура  посе кнопки 'БАН'
def ban(message):
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='БАН ВО ВСЕХ ГРУППАХ', callback_data='ban_all')
    item2 = types.InlineKeyboardButton(text='ВЫБРАТЬ ГРППУ', callback_data='ban_vib')
    item3 = types.InlineKeyboardButton(text='ГЛАВНАЯ', callback_data='glav')

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, 'Выберите один из вариантов', reply_markup=markup)


# Клавиатура  посе кнопки 'РАЗБАН'
def unban(message):
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='РАЗБАН ВО ВСЕХ ГРУППАХ', callback_data='unban_all')
    item2 = types.InlineKeyboardButton(text='ВЫБРАТЬ ГРППУ', callback_data='unban_vib')
    item3 = types.InlineKeyboardButton(text='ГЛАВНАЯ', callback_data='glav')

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, 'Выберите один из вариантов', reply_markup=markup)