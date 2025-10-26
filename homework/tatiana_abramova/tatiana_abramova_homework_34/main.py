import time
from time import sleep


while True:
    print("Привет из Docker! Текущее время:", time.strftime("%H:%M:%S"))
    sleep(3)
