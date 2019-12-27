import datetime
import requests
import vk_api

from bs4 import BeautifulSoup
from random import randint
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token='3ae03ce89d13effca33ecac09e6919dd03eb1b4dc4b55fe33075c16ae6ad90f4b58fcb724b2b6fc07826b')
longpoll = VkLongPoll(vk_session)

STATE = 'idle'

# import gspread
# from oauth2client.service_account import ServiceAccountCredentials
# scope = ['https://spreadsheets.google.com/feeds',
#          'https://www.googleapis.com/auth/drive']
# creds = ServiceAccountCredentials.from_json_keyfile_name('Secret.json',
#                                                          scope)
# client = gspread.authorize(creds)

user_old = dict()
def send(mess):
    vk.messages.send(
        user_id=event.user_id,
        keyboard=StartKeyboard.get_keyboard(),
        message=mess, random_id=randint(0, 2147483647))


vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        event.text = event.text.lower()

        if event.text == 'start' or event.text == 'начать':
                StartKeyboard = VkKeyboard(one_time=True)
                StartKeyboard.add_button('Добавить форму', color=VkKeyboardColor.DEFAULT)
                send('Привет''&#128075;')
                STATE = 
        
        else:
            send('ERROR')
