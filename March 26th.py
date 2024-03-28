import random

print("동전 던지기 게임을 시작합니다.")

coin = random.randint(2)

if coin == 0:
    print("앞면 입니다.")
else:
    print("뒷면 입니다.")

print("게임이 종료되었습니다.")