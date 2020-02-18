import random

result = []  # 결과를 누적할 리스트
win = 0  # 승
lose = 0  # 패
draw = 0  # 무
while True:
    me1 = input("가위 바위 보! (종료 x)>> ")  # 내가 낼 것 입력
    if me1 == "가위": pass
    elif me1 == "바위": pass
    elif me1 == "보": pass
    elif (me1 == "x" or me1 == "X"):
        print("게임을 종료합니다.")
        break
    else:
        print("잘못 입력하셨습니다.")
        continue
    com = random.choice(["가위", "바위", "보"])  # 컴퓨터가 낼 것
    print("컴퓨터는? %s" % com)
    if me1 == com:
        print("비겼습니다.")
        result.append("비김")
    elif me1 == "가위":
        if com == "바위":
            print("졌습니다.")
            result.append("패")
        else:
            print("이겼습니다.")
            result.append("승")
    elif me1 == "바위":
        if com == "보":
            print("졌습니다.")
            result.append("패")
        else:
            print("이겼습니다.")
            result.append("승")
    else:
        if com == "보":
            print("졌습니다.")
            result.append("패")
        else:
            print("이겼습니다.")
            result.append("승")
print("결과: %s" % result)
for x in result:
    if x == "승": win = win + 1
    elif x == "패": lose = lose + 1
    else: draw = draw + 1
print("총 %d전 %d승 %d무 %d패" % (len(result), win, draw, lose))
