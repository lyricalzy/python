# 극장 예매시스템
# 1. 화면을 만든다.
# 0이 10개 들아간 리스트 필요!
seat = [0] * 10
# ctrl + alt + ↓ = 한줄복사
name = input("이름을 입력해주세요: ")
print("어서오세요. %s님" % name)
while True:
    print("\n-----------------------------")
    for i in range(1, len(seat) + 1):
        print(i, end="  ")
    print("\n-----------------------------")

    # 자리 예약 상태 프린트(0 => 예약x, 1 => 예약o)
    for x in seat:
        print(x, end="  ")
    print("\n-----------------------------")

    # 입력값은 리스트의 인덱스로 사용
    print("참고: 0 => 예약x, 1 => 예약o")
    reserve = int(input("원하는 좌석 번호 입력(종료: -1)>> "))
    if reserve == -1:
        # 종료시 영수증 출력
        print("%s님의 예매 확인 영수증입니다." % name)
        print("-------------------------------")
        print("예매된 좌석 번호는", end=" ")
        for j in range(0, len(seat)):
            if seat[j] == 1:
                print("%d번" % (j + 1), end=" ")
        print("\n전체 예매된 좌석수는 %d좌석" % seat.count(1))
        print("결제 금액은 %d원입니다." % (seat.count(1) * 10000))
        print("-------------------------------")
        print("예매 프로그램을 종료합니다.")
        break
    # 좌석 범위를 벗어난 경우 다시 처음으로 돌아감
    elif (reserve > 10 or reserve < 0):
        print("잘못입력하셨습니다. 다시 입력해주세요.")
        continue

    # 인덱스는 좌석 번호
    print("%d번 좌석을 선택하셨습니다." % reserve)

    # 이미 예매되어있는 좌석인 경우 => 불가능하다고 처리
    if seat[reserve - 1] == 1:
        print("이미 예약된 좌석입니다. 다시 선택해주세요.")
    # 예매되어있지 않은 좌석인 경우 => 가능하다고 처리
    else:
        seat[reserve - 1] = 1
        print("예매 처리를 완료했습니다.")
        print("현재 예매된 좌석 수는 %d석입니다." % seat.count(1))
