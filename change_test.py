
list_vending_name = ["콜라", "사이다", "환타", "라떼", "아메리카노", "카푸치노", "홍차"] #판매 음료 종류 저장 리스트
list_vending_count = [10, 10, 10, 10, 10, 10, 10]  # 각 음료 갯수
list_vending_sum = [1000, 900, 800, 1500, 1000, 1000, 800]  #각 음료 가격
user_vending_count = [0, 0, 0, 0, 0, 0, 0]       #내가 구매한 음료 갯수
vending_change_count = [10, 10, 10]          #자판기에 남은 음료 개수
card_sum = 10000             #카드 잔액 1만원 설정
user_choice = input("무엇으로 결제하시겠습니까?(카드,현금): ")   #카드로 결제할지 현금으로 결제할지 선택
if user_choice == "현금":                                 #현금으로 결제 선택시
    user_insert = int(input("얼마를 넣으시겠습니까?: "))    #얼마를 넣을지 물어봄
while True:   #반복문
    if user_choice == "현금":     #현금으로 결제시
        user_want = input("어떤 음료를 고르시겠습니까?(종료:x): ")  #고를 음료 선택(종료는 x)
        if user_want != "x":   # x버튼을 누를떄의 경우를 고려하지 않으면 후반 코드가 꼬이므로 설정
            if user_want == "라떼" or user_want == "아메리카노" or user_want == "카푸치노" or user_want == "홍차":
                while True:   #라뗴,아메리카노,카푸치노,홍차 선택시 hot,cool중 무엇을 고를지 물어봄
                    cold_hot = input("hot,cool 중 무엇을 선택하실건가요?: ")
                    if cold_hot == "hot" or cold_hot == "cool":
                        break
                    else:     #hot,cool 외 실수로 다른 입력시 잘못 입력 전시하고 다시 물어봄
                        print("잘못 입력하셨습니다.")
            list_vending_count[list_vending_name.index(user_want)] -= 1   #음료를 고르면 자판기 내 해당 잔고가 1개씩 줄어듬
            user_vending_count[list_vending_name.index(user_want)] += 1   #음료를 고르면 내가 구매한 음료리스트 해당 개수가 1개씩 늘음
            if user_insert < list_vending_sum[list_vending_name.index(user_want)]: #사고픈 음료가 내가 낸 금액의 잔액보다 높으면
                print("잔액이 부족합니다.")                                         #잔액이 부족합니다 전시 후 구매 반복문 종료 후
                print("구매를 종료합니다.")                                         #잔액,구매한 음료 개수, 1000원,500원,100원 개수
                print("----------------------------------")                        #전시
                print("잔액은", str(user_insert) + "원 입니다.")
                thousand = user_insert // 1000
                five_hunred = (user_insert % 1000) // 500
                hunred = ((user_insert % 1000) % 500) // 100
                vending_change_count[0] = vending_change_count[0] - thousand
                vending_change_count[1] = vending_change_count[1] - five_hunred
                vending_change_count[2] = vending_change_count[2] - hunred
                if thousand > 10:                                    #자판기 내 1000원의 개수가 부족하면 500원을 대신
                    five_hunred += (thousand - 10) * 1000 // 500     #500원이 부족하면 100원을 대신 거슬러주고
                    thousand = 10                                    #100원도 부족하면 거스름돈 부족 전시
                if five_hunred > 10:
                    hunred += (five_hunred - 10) * 500 // 100
                    five_hunred = 10
                if hunred > 10:
                    print("거스름 돈이 부족합니다.  02-222-3333으로 문의 주세요")
                    hunred = 10
                print("1000원:", str(thousand) + "장", "500원:", str(five_hunred) + "개", "100원:", str(hunred) + "개")
                break
            if list_vending_count[list_vending_name.index(user_want)] <0: #고른 음료의 자판기 내 잔고가 0개면
                print(user_want + "는 품절입니다.")                         # 품절입니다 전시 후 다시입력
                print("죄송하지만 다른 음료를 선택해주세요.")
            else:
                user_insert -= list_vending_sum[list_vending_name.index(user_want)] #음료 구매시마다 내가 낸 금액 감소
        print("잔액은", str(user_insert) + "원 입니다.")
        if user_want == "x":    #x를 누르면
            print("구매를 종료합니다.")  #구매 종료 후
            print("----------------------------------")
            print("잔액은", str(user_insert) + "원 입니다.")  #위와 같은 구매 종료 후 정보들 프린트
            thousand = user_insert // 1000
            five_hunred = (user_insert % 1000) // 500
            hunred = ((user_insert % 1000) % 500) // 100
            vending_change_count[0] = vending_change_count[0] - thousand
            vending_change_count[1] = vending_change_count[1] - five_hunred
            vending_change_count[2] = vending_change_count[2] - hunred
            if thousand > 10:
                five_hunred += (thousand-10) * 1000 // 500
                thousand = 10
            if five_hunred > 10:
                hunred += (five_hunred-10) * 500 // 100
                five_hunred = 10
            if hunred>10:
                print("거스름 돈이 부족합니다.  02-222-3333으로 문의 주세요")
                hunred=10
            print("1000원:", str(thousand) + "장", "500원:", str(five_hunred) + "개", "100원:", str(hunred) + "개")
            break
    elif user_choice == "카드":    #카드를 선택시
        user_want = input("어떤 음료를 고르시겠습니까?(종료:x): ")  #넣을 금액을 물어보지 않고 바로 음료 선택
        if user_want != "x":                    #여기부턴 위 현금결제와 일치
            if user_want == "라떼" or user_want == "아메리카노" or user_want == "카푸치노" or user_want == "홍차":
                while True:
                    cold_hot = input("hot,cool 중 무엇을 선택하실건가요?: ")
                    if cold_hot == "hot" or cold_hot == "cool":
                        break
                    else:
                        print("잘못 입력하셨습니다.")
            list_vending_count[list_vending_name.index(user_want)] -= 1
            user_vending_count[list_vending_name.index(user_want)] += 1

            if card_sum < list_vending_sum[list_vending_name.index(user_want)]:
                print("잔액이 부족합니다.")
                print("구매를 종료합니다.")
                print("----------------------------------")
                print("잔액은", str(card_sum) + "원 입니다.")
                thousand = card_sum // 1000
                five_hunred = (card_sum % 1000) // 500
                hunred = ((card_sum % 1000) % 500) // 100
                vending_change_count[0] = vending_change_count[0] - thousand
                vending_change_count[1] = vending_change_count[1] - five_hunred
                vending_change_count[2] = vending_change_count[2] - hunred
                if thousand > 10:
                    five_hunred += (thousand - 10) * 1000 // 500
                    thousand = 10
                if five_hunred > 10:
                    hunred += (five_hunred - 10) * 500 // 100
                    five_hunred = 10
                if hunred > 10:
                    print("거스름 돈이 부족합니다.  02-222-3333으로 문의 주세요")
                    hunred = 10
                print("1000원:", str(thousand) + "장", "500원:", str(five_hunred) + "개", "100원:", str(hunred) + "개")
                break
            if list_vending_count[list_vending_name.index(user_want)] < 0:
                print(user_want + "는 품절입니다.")
                print("죄송하지만 다른 음료를 선택해주세요.")
            else:
                card_sum -= list_vending_sum[list_vending_name.index(user_want)]
        print("잔액은", str(card_sum) + "원 입니다.")
        if user_want == "x":
            print("구매를 종료합니다.")
            print("----------------------------------")
            print("구매한 음료는", end=" ")
            for i in range(7):
                if user_vending_count[i] != 0:
                    print(list_vending_name[i] + ":", str(user_vending_count[i]) + "개", end=" ")
            print()
            print("잔액은", str(card_sum) + "원 입니다.")
            thousand = card_sum // 1000
            five_hunred = (card_sum % 1000) // 500
            hunred = ((card_sum % 1000) % 500) // 100
            vending_change_count[0] = vending_change_count[0] - thousand
            vending_change_count[1] = vending_change_count[1] - five_hunred
            vending_change_count[2] = vending_change_count[2] - hunred
            if thousand > 10:
                five_hunred += (thousand - 10) * 1000 // 500
                thousand = 10
            if five_hunred > 10:
                hunred += (five_hunred - 10) * 500 // 100
                five_hunred = 10
            if hunred > 10:
                print("거스름 돈이 부족합니다.  02-222-3333으로 문의 주세요")
                hunred = 10
            print("1000원:", str(thousand) + "장", "500원:", str(five_hunred) + "개", "100원:", str(hunred) + "개")
            break