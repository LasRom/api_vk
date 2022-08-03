import vk_api
import datetime
import time

schet = 1000
vk = vk_api.VkApi(
        token="")
last_dt = datetime.datetime.now()
while True:
    try:
        if str(last_dt).split()[1].split(':')[1] != str(datetime.datetime.now()).split()[1].split(':')[1]:
            print(1)
            dt = datetime.datetime.now()
            vk.method("status.set", {"text": f'{dt.strftime("Date: %d-%m-%Y  time: %H:%M")}'})
            last_dt = datetime.datetime.now()
            time.sleep(60)
        else:
            print(2)
            continue
    except BaseException as e:
        print(e)
        vk = vk_api.VkApi(
            token="")
