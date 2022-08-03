import vk_api
import datetime
import time

vk = vk_api.VkApi(
    token="your_token")
last_dt = datetime.datetime.now()  # получаю текущую дату и время
while True:
    # проверяю, прошла ли минута, чтобы обновить статус
    if str(last_dt).split()[1].split(':')[1] != str(datetime.datetime.now()).split()[1].split(':')[1]:
        dt = datetime.datetime.now()  # получаю текущую дату и время
        vk.method("status.set", {"text": f'{dt.strftime("Date: %d-%m-%Y  time: %H:%M")}'})  # обновляю статус
        last_dt = dt  # меняю последнее время
        time.sleep(60)  # заставляем код "заснуть", чтобы обойти капчу вк
