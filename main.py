# from db import cursor, conn
# from config import TOKEN
# from random import shuffle
# import requests



# def create_table_user():
#     query = """
#     CREATE TABLE IF NOT EXISTS users (
#         id SERIAL PRIMARY KEY,
#         name VARCHAR, 
#         user_id VARCHAR,
#         group_name VARCHAR);"""

#     cursor.execute(query=query)
#     conn.commit()
#     print('create table users success!')


# def insert_user(name, user_id, group_name):
#     query = f"""
#         INSERT INTO users (name, user_id, group_name)
#         VALUES('{name}', '{user_id}', '{group_name}');"""
#     cursor.execute(query=query)
#     conn.commit()

# def create_group(group_name: str):
#     query = f"""
#     CREATE TABLE IF NOT EXISTS {group_name} (
#         user_name VARCHAR ,
#         phone_number VARCHAR,
#         first_name VARCHAR,
#         last_name VARCHAR,
#         chat_id INT,
#         password VARCHAR);"""
#     cursor.execute(query=query)
#     conn.commit()

# def add_to_group(group_name, user_name, phone_number, first_name: str, last_name: str, chat_id: int, password):
#     query = f"""
#         INSERT INTO {group_name}( user_name, phone_number, first_name, last_name, chat_id, password )
#         VALUES( '{user_name}', '{phone_number}', '{first_name}', '{last_name}', {chat_id}, '{password}');"""
#     cursor.execute(query = query)
#     conn.commit()

# def is_user_exists(chat_id: int, group_name) -> bool:
#     query = f"""
#         SELECT * from {group_name} where chat_id = {chat_id};"""
#     cursor.execute(query=query)
#     response = cursor.fetchone()
#     if response:
#         return True
#     return False

# def create_mix_table(group_name):
#     query = f"""
#         CREATE TABLE IF NOT EXISTS mix_{group_name}(
#             santa INT,
#             pupsic INT);"""
#     cursor.execute(query=query)
#     conn.commit()

# def get_user(group_name):
#     query = f"""
#         SELECT * 
#         FROM {group_name};"""
#     cursor.execute(query=query)
#     response = cursor.fetchall()
#     pupsic_list1 = [i[-2] for i in response]
#     shuffle(pupsic_list1)
#     mix = {
#         pupsic: pupsic_list1[pupsic_list1.index(pupsic)-1] for pupsic in pupsic_list1
#     }     
#     return mix

# def insert_mix(group_name, santa, pupsic):
#     query = f"""
#         INSERT INTO mix_{group_name}(santa, pupsic)
#         VALUES ({santa}, {pupsic});"""
#     cursor.execute(query= query)
#     conn.commit()

# def mix_user(user_id):
#     for key, value in get_user(group_name= get_autor(user_id= user_id)).items():
#         print(key, value)


# def get_name(user_id):
#     query = f"""
#         SELECT name FROM users WHERE chat_id = {user_id};"""
#     cursor.execute(query= query)
#     response = cursor.fetchall()
#     return response[0]

# def create_table_mix():
#     query = """
#         CREATE TABLE IF NOT EXISTS mix(
#             santa   INT,
#             pupsic INT
#         ); """
#     cursor.execute(query= query)
#     conn.commit()
#     print("Table created successfully")

# # def mix_add():
# #     for key, value in mix_user().items():
# #         # insert_mix(key, value)
# #         insert_mix(key, value)



# def create_groups():
#     query = """
#         CREATE TABLE IF NOT EXISTS groups (
#             id SERIAL PRIMARY KEY,
#             group_name VARCHAR,
#             group_password VARCHAR,
#             autor VARCHAR);"""
#     cursor.execute(query=query)
#     conn.commit()
#     print('created groups table successfully')


# def insert_groups(group_name, group_password, autor):
#     query = f"""
#         INSERT INTO groups (group_name, group_password, autor)
#         VALUES ('{group_name}', '{group_password}', '{autor}');"""
#     cursor.execute(query= query)
#     conn.commit()

# def is_group_exists(group_name):
#     query = f"""
#         SELECT group_name FROM groups WHERE group_name = '{group_name}';"""
#     cursor.execute(query= query)
#     response = cursor.fetchone()
#     print(response)
#     if response:
#         return True
#     return False
    
# def check_password(group_name):
#     query = f"""
#         SELECT group_password FROM groups
#         WHERE group_name = '{group_name}';"""
#     cursor.execute(query= query)
#     response = cursor.fetchall()
#     return response[0]

# def get_autor(user_id):
#     query = f"""
#         SELECT group_name FROM groups WHERE autor = '{user_id}';"""
#     cursor.execute(query= query)
#     response = cursor.fetchone()
#     return response[0]

# def get_name_from_mix(group_id):
#     query = f"""
#         SELECT * FROM mix_{group_id};"""
#     cursor.execute(query= query)
#     response = cursor.fetchone()
#     return response
# # print(get_name_from_mix('qwerty'))

# def select_users_from_group(group_name):
#     query = f"""
#         SELECT user_name FROM {group_name};""" 
#     cursor.execute(query = query)
#     response = cursor.fetchall()
#     text = ''
#     for i in response:
#         text = text + i[0] + '\n'
#     return text

# def send_message_telebot(chat_id, group_id):
#     text = get_name_from_mix(group_id)
#     send_text = 'https://api.telegram.org/bot' + TOKEN + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + text
#     requests.get(send_text)














a = int(input(''))
b = int(input(''))

if a > b:
    print(2)
elif a < b:
    print(1)
else:
    print('olar ten')