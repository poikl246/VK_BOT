import os
import random
import foto
import requests
import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

session = requests.Session()
vk_session = vk_api.VkApi(token='b573f48e2626f7eb519c57dd2c9310de599e94fb6aea392c7adbcf9e1a5355910d71656f49139736be078')
upload = VkUpload(vk_session)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()



print('Поехали')

def upload_photo(upload, name):
    response = upload.photo_messages(foto.main(name=name, foto_n = random.randint(0, len(os.listdir("foto")))))[0]

    owner_id = response['owner_id']
    photo_id = response['id']
    access_key = response['access_key']
    print(owner_id, photo_id, access_key)

    return owner_id, photo_id, access_key


def send_photo(vk, peer_id, owner_id, photo_id, access_key):
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'
    print(attachment)
    vk.messages.send(
        random_id=get_random_id(),
        peer_id=peer_id,
        attachment=attachment
    )






img = r'hello.png'

def bot():
    print('start')
    for event in longpoll.listen():
        # print(123)
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
       #Слушаем longpoll, если пришло сообщение то:
            # 😂🤣😅😆😇
            massage = str(event.text.lower()).replace(')', '').replace(',', '').replace('😂', '').replace('🤣', '').replace('😅', '').replace('😆', '').replace('😇', '')
            print(massage)
            if massage == 'привет!' or massage == 'привет!!' or massage == 'привет!!!' or massage == 'привет' or massage == 'приветик' or massage == 'здравствуйте' or massage == 'приветствую' or massage == 'здорово' or massage == 'салют': #Если написали заданную фразу
                vk.messages.send( #Отправляем сообщение
                    user_id=event.user_id,
                    message='Привет, напиши, кому сделать валентинку',
                    random_id=get_random_id())

            elif massage in 'хочу' or massage == '':
                vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    message='Кому сделать валентинку?))',
                    random_id=get_random_id())

            elif massage == 'мне' or massage == 'мне)' or massage == 'мне))' or massage == 'мне)))':
                vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    message='Сейчас сделаю)',
                    random_id=get_random_id())

                send_photo(vk, event.user_id, *upload_photo(upload, 'Тебе)))'))

            elif massage in 'опа ого спасибо ооо ахаххахахаа ваау вааау ваааау вааааау клаасс класс вау ух-ты ухты ух ты фигасе хренасе ого офигеть охренеть спасибо вам спс пасиб пасибо':
                vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    message='Рады что тебе нравится, можешь сделать еще. Если хочешь, то напиши на кого сделать))',
                    random_id=get_random_id())

            else:
                vk.messages.send( #Отправляем сообщение
                    user_id=event.user_id,
                    message='Сейчас сделаю)',
                    random_id=get_random_id())

                try:
                    send_photo(vk, event.user_id, *upload_photo(upload, event.text))
                except:
                    try:
                        send_photo(vk, event.user_id, *upload_photo(upload, event.text))
                    except:
                        vk.messages.send(  # Отправляем сообщение
                            user_id=event.user_id,
                            message='Ошибка',
                            random_id=get_random_id())



if __name__ == '__main__':
    while True:
        try:
            bot()
        except:
            print('Бот упал, запускаю еще раз')
            session = requests.Session()
            vk_session = vk_api.VkApi(
                token='b573f48e2626f7eb519c57dd2c9310de599e94fb6aea392c7adbcf9e1a5355910d71656f49139736be078')
            upload = VkUpload(vk_session)
            longpoll = VkLongPoll(vk_session)
            vk = vk_session.get_api()