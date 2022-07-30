import vk_api
import time

schet = 1000
while True:
    vk = vk_api.VkApi(
        token="vk1.a.SCUc7l99Tw9EZUUbsot_rMkXAX3WnUAJvdgjoYQB78CcB-L8sFTGSnbDycjdjEemMmYX6h09deQdwvNDVtYjzywHr39U6FH5tVvI1cdtg41l48-KAE_NY5Sjf5nhCYPrOafBM-4fcJbHbM6nfqAS5TcaQVDLBYUGkByzzdw2MPp6v8Ftq-HsIPh8LaBNMHQM")
    vk.method("status.set", {"text": f"1000 - 7 (online every 30 seconds) {schet}"})
    schet -= 7
    if schet < 0:
        schet = 1000
    time.sleep(30)  # погружаем скрипт в «сон» на 30 секунд
