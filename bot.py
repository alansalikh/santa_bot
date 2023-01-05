import telebot
from telebot import types

from main import *
from config import TOKEN

contact_user = {}
group = {'': ''}
abc = ['', '']

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message: types.Message):
    bot.delete_message(message.chat.id, message.message_id)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True).add(types.KeyboardButton('/room'))
    text = "Привет это Санта бот, для продолжения найди или создай группу"
    bot.send_message(message.chat.id, text=text, reply_markup=markup)


@bot.message_handler(commands=['room'])
def group_add(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True).add(types.KeyboardButton('Создать группу'),types.KeyboardButton('Присоединиться к группе'))
    gif_animation = open('img/123.gif', 'rb')
    bot.send_animation(message.chat.id,gif_animation)
    msg = bot.send_message(message.chat.id, 'Вы можете создать для друзей группу или же присоединиться в группу', reply_markup=markup) 
    bot.register_next_step_handler(msg, groupp)
def groupp(message: types.Message):
    text = message.text
    if text == 'Создать группу':
        group_name = bot.send_message(message.chat.id, 'Введите название группы')
        bot.register_next_step_handler(group_name, name_group)
    elif text == 'Присоединиться к группе':
        join = bot.send_message(message.chat.id, 'Напишите называние группы')
        bot.register_next_step_handler(join, join_group)
    else:
        bot.send_message(message.chat.id,text='Вы можете создать для друзей группу или же присоединиться в группу')
def join_group(message: types.Message):
    if is_group_exists(message.text):
        abc[0] = message.text
        abc[1] = (check_password(message.text))
        join = bot.send_message(message.chat.id, 'Теперь пароль от группы')
        bot.register_next_step_handler(join, check_password)
    else:
        bot.send_message(message.chat.id, 'Не правильное название группы')

def check_password(message: types.Message):
    if message.text in abc[1]:
        group[abc[0]] = message.text
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True).add(types.KeyboardButton('Зарегистрироваться', request_contact=True))
        bot.send_message(message.chat.id, 'вы прошли проверку по паролю')
        bot.send_message(message.chat.id, 'Для продолжения зарегиструйтесь', reply_markup= markup)

    else:
        bot.send_message(message.chat.id, 'ваш пароль не верный')

def name_group(message: types.Message):    
    if is_group_exists(message.text):
        msg = bot.send_message(message.chat.id, 'такая группа уже существует, придумайте новое называние')
        bot.register_next_step_handler(msg, name_group)
    else:
        msg = bot.send_message(message.chat.id, 'теперь пароль от комнаты')
        bot.register_next_step_handler(msg, password)
        abc[0] = message.text
        if ' ' in message.text:
            abc[0] = message.text.replace(' ', '_')
    print(abc[0])



    
def password(message: types.Message):
       
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True).add(types.KeyboardButton('Зарегистрироваться', request_contact=True))
    group[abc[0]] = message.text
    print(abc[0])
    create_group(abc[0])
    insert_groups(abc[0], message.text, message.chat.id)
    create_mix_table(abc[0])
    bot.send_message(message.chat.id, 'Вы успешно зарегистровались')
    bot.send_message(message.chat.id, 'Для продолжения зарегиструйтесь', reply_markup= markup)
    # except:
    #     msg = bot.send_message(message.chat.id, 'произошла ошибка попробуйте заново')   
    #     bot.register_next_step_handler(msg, password)
    #     print(message.chat.id)
@bot.message_handler(content_types=['contact'])
def contact(message: types.Message):
    if message.contact is not None:
        print(abc[0])
        if not is_user_exists(message.chat.id, group_name= abc[0]):
            contact_user[message.chat.id] = message.contact.phone_number
            chat_id = message.chat.id
            msg = bot.send_message(chat_id, 'отпрвьте свое полное имя')
            bot.register_next_step_handler(msg, name)
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True).add(types.KeyboardButton('да'), types.KeyboardButton('нет'))
            bot.send_message(message.chat.id, 'Вы уже зарегистрованы')
            msg = bot.send_message(message.chat.id, 'если вы автор группы вы можете посмотреть участников группы, вы создатель?', reply_markup= markup)
            bot.register_next_step_handler(msg, check_autor)
    
def name(message: types.Message):
    name = message.text
    print(name)
    if not is_user_exists(message.chat.id, group_name= abc[0]):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True).add(types.KeyboardButton('да'), types.KeyboardButton('нет'))
        add_to_group(group_name = abc[0], user_name=name, phone_number= contact_user[message.chat.id], first_name= message.from_user.first_name, last_name= message.from_user.last_name, chat_id= message.chat.id, password=group[abc[0]])
        bot.send_message(message.chat.id, 'Вы успешно зарегистровались!')
        insert_user(name= name, user_id= message.chat.id, group_name= abc[0])
        msg = bot.send_message(message.chat.id, 'если вы автор группы вы можете посмотреть участников группы, вы создатель?', reply_markup= markup)
        bot.register_next_step_handler(msg, check_autor)
            
    else:
        bot.send_message(message.chat.id, 'Вы уже зарегистрованы')

def check_autor(message: types.Message):
    if message.text == 'да':
        msg = bot.send_message(message.chat.id, 'называние группы?')
        bot.register_next_step_handler(msg, autor)
    elif message.text == 'нет':
        bot.send_message(message.chat.id, 'ждите пока автор группы не отправит запрос')

def autor(message: types.Message):
    try:
        if message.text == get_autor(message.chat.id):
            bot.send_message(message.chat.id, text= select_users_from_group(message.text))
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True).add(types.KeyboardButton('да'), types.KeyboardButton('нет'))
            msg = bot.send_message(message.chat.id, text='хотите начать игру?', reply_markup= markup)
            bot.register_next_step_handler(msg, mix)
        else:
            bot.send_message(message.chat.id, text='такой группы не существует или вы не ее создательь')
    except:
        bot.send_message(message.chat.id, text='такой группы не существует или вы не ее создатель')
        
def mix(message: types.Message):
    if message.text == 'да':
        mix_user(message.chat.id)
        # send_message_telebot(message.chat.id, abc[0])
    elif message.text == 'нет':
        bot.send_message(message.chat.id, 'напишите да когда захотите начать игру')
    else:
        bot.send_message(message.chat.id, text='не известная команда')



# @bot.message_handler(commands=['start', 'go'])
# def start_handler(message):
#     chat_id = message.chat.id
#     text = message.text
#     msg = bot.send_message(chat_id, 'Сколько вам лет?')
#     bot.register_next_step_handler(msg, askAge)

# def askAge(message):
#     chat_id = message.chat.id
#     text = message.text
#     if not text.isdigit():
#         msg = bot.send_message(chat_id, 'Возраст должен быть числом, введите ещё раз.')
#         bot.register_next_step_handler(msg, askAge) #askSource
#         return
#     msg = bot.send_message(chat_id, 'Спасибо, я запомнил что вам ' + text + ' лет.')

# @bot.message_handler(content_types=['text'])
# def send_name(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     item1 = types.KeyboardButton('Найти пупсика')
#     markup.add(item1)
#     bot.send_message(message.chat.id, 'Введите сове имя(полное)', reply_markup=markup)
#     bot.send_message(message.chat.id, message.text)
# @bot.message_handler()
# def name(message: types.Message):
#     if message.text.type == 'private':
#         insert_name(message.text)
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         item1 = types.KeyboardButton('')
# @bot.message_handler(content_types=['text'])
# def text(message: types.Message):
#     if message.chat.type == 'private':
#         if message.text.lower() == 'найти пупсика':

if __name__ == '__main__':

    bot.polling(non_stop=True)
