from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api
import json
import DayBack
import datetime
import AdminPermissions
import wget
import os
import shutil
import re

keyboard = {
    "one_time": False,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": "Расписание на сегодня"
            },
            "color": "positive"
        },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Расписание на завтра"
                },
                "color": "positive"
            },
        ],
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Понедельник"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Вторник"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Среда"
                },
                "color": "primary"
            }
        ],
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Четверг"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Пятница"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Суббота"
                },
                "color": "primary"
            }
        ]

    ]
}

keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))

# Работа с ВК

vk = vk_api.VkApi(token="a0400d7371965dfb96d693d6e4d3ea51c7463ec6b84da6f54cb2b844713a8563b7ece2c7d2896b7964d18")

vk._auth_token()

vk.get_api()

longpoll = VkBotLongPoll(vk, 191681643)

canshowmessagesender = True

stuts = dict()
fullusername = ''

while True:
    try:
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                classNumber = "P"
                if ("!расписание" in event.object.text) and (str(event.object.from_id) in AdminPermissions.GetAdm()):

                    file_url = event.object.attachments[0]['doc']['url']
                    raspname = event.object.attachments[0]['doc']['title']

                    raspname = re.sub(r" ", "", raspname)
                    print("Tut")
                    raspname = raspname.replace('(', '')
                    raspname = raspname.replace(')', '')
                    filename = wget.download(file_url)
                    os.rename(filename, raspname)

                    shutil.move('../gitHome/' + str(raspname), '../gitHome/ExcelStorage/')
                    print("Расписание обновлено на" + str(raspname))
                    L = 0
                    for i in AdminPermissions.GetAdm():
                        L += 1
                        if (canshowmessagesender):
                            vk.method("messages.send", {"user_id": AdminPermissions.GetAdm()[L - 1],
                                                        "message": "Расписание обновлено на: " + raspname,
                                                        "random_id": 0})

                # print(event.object)
                if event.object.peer_id != event.object.from_id:
                    if (event.object.text.lower() == "!") or (event.object.text.lower() == "начать"):
                        vk.method("messages.send",
                                  {"peer_id": event.object.from_id, "message": ")", "keyboard": keyboard,
                                   "random_id": 0})



                elif event.object.peer_id == event.object.from_id:
                    fulluserinfo = vk.method("users.get", {"user_id": event.object.from_id})
                    fullusername = str(fulluserinfo[0]['first_name']) + " " + str(fulluserinfo[0]['last_name'])

                    if (event.object.text.lower() == "!") or (event.object.text.lower() == "начать"):
                        vk.method("messages.send",
                                  {"peer_id": event.object.from_id, "message": ")", "keyboard": keyboard,
                                   "random_id": 0})

                    if event.object.text.lower() == "привет":
                        vk.method("messages.send", {"user_id": event.object.from_id, "message": event.object.text,
                                                    "random_id": 0})
                    if (event.object.text.lower() == "р") or (event.object.text == "!"):
                        vk.method("messages.send", {"peer_id": event.object.from_id, "message": ")",
                                                    "keyboard": keyboard, "random_id": 100})

                    if "Понедельник" in event.object.text:
                        vk.method("messages.send",
                                  {"user_id": event.object.from_id, "message": DayBack.Back(0, classNumber),
                                   "random_id": 0})
                    if "Вторник" in event.object.text:
                        vk.method("messages.send",
                                  {"user_id": event.object.from_id, "message": DayBack.Back(1, classNumber),
                                   "random_id": 0})
                    if "Среда" in event.object.text:
                        vk.method("messages.send",
                                  {"user_id": event.object.from_id, "message": DayBack.Back(2, classNumber),
                                   "random_id": 0})
                    if "Четверг" in event.object.text:
                        vk.method("messages.send",
                                  {"user_id": event.object.from_id, "message": DayBack.Back(3, classNumber),
                                   "random_id": 0})
                    if "Пятница" in event.object.text:
                        vk.method("messages.send",
                                  {"user_id": event.object.from_id, "message": DayBack.Back(4, classNumber),
                                   "random_id": 0})
                    if "Суббота" in event.object.text:
                        vk.method("messages.send",
                                  {"user_id": event.object.from_id, "message": DayBack.Back(5, classNumber),
                                   "random_id": 0})

                    if "Расписание на сегодня" in event.object.text:
                        vk.method("messages.send", {"user_id": event.object.from_id, "message": DayBack.Back(
                            datetime.datetime.weekday(datetime.datetime.now()), classNumber),
                                                    "random_id": 0})
                    if "Расписание на завтра" in event.object.text:
                        vk.method("messages.send", {"user_id": event.object.from_id, "message": DayBack.Back(
                            datetime.datetime.weekday(datetime.datetime.now()) + 1, classNumber),
                                                    "random_id": 0})

                    # cnf-выключает уведомление о тем, кто пользовался ботом, cnt-включает
                    if (("s" in event.object.text) or ("cnf" in event.object.text)) and (
                            str(event.object.from_id) in (AdminPermissions.GetAdm())):
                        canshowmessagesender = False
                    if ("cnt" in event.object.text) and (str(event.object.from_id) in (AdminPermissions.GetAdm())):
                        canshowmessagesender = True
                    L = 0
                    for i in AdminPermissions.GetAdm():
                        L += 1
                        if (canshowmessagesender):
                            vk.method("messages.send", {"user_id": AdminPermissions.GetAdm()[L - 1],
                                                        "message": "Ботом воспользовался: " + fullusername,
                                                        "random_id": 0})

                    # Система watch status
                    if (fullusername not in stuts):
                        stuts[fullusername] = 0

                    if (fullusername in stuts):
                        stuts[fullusername] += 1
                    print(stuts)


                    def readystut(stutus):
                        ready = ''
                        for key in stuts:
                            ready += str(key) + " " + str(stuts[key]) + "\n"
                        return ready


                    if ("stut" in event.object.text) and (str(event.object.from_id) in (AdminPermissions.GetAdm())):
                        vk.method("messages.send", {"user_id": event.object.from_id,
                                                    "message": readystut(stuts), "random_id": 0})

                    if ("версия" in event.object.text):
                        vk.method("messages.send", {"user_id": event.object.from_id,
                                                    "message": "Версия расписания: " + str(DayBack.LastRasp()),
                                                    "random_id": 0})








    except:
        print("")
