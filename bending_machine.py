food_list = ["포카리", "코카콜라", "레쓰비", "초코송이", "빼빼로", "다이제", "자일리톨"]  # 간식 리스트
price_list = [800, 800, 600, 900, 1000, 1500, 1000]  # 간식의 가격 리스트
stock_list = [7, 6, 4, 5, 7, 0, 8]  # 간식의 재고 리스트
select_list = []  # 내가 고른 장바구니
select_list2 = [0, 0, 0, 0, 0, 0, 0]  # 장바구니에 들어간 수량
full_price = 0  # 고른 간식의 총액
change = 0  # 잔돈

while True:
    print("--------------------------------------------------")
    for i in range(0, len(food_list)):  # 간식 리스트 출력
        print(food_list[i], end=" ")
    print("\n--------------------------------------------------")
    for j in range(0, len(price_list)):  # 간식의 가격 리스트 출력
        print(price_list[j], end="    ")
    print("\n--------------------------------------------------")
    for k in range(0, len(stock_list)):  # 간식의 수량 리스트 출력
        print(stock_list[k], end="      ")
    print("\n--------------------------------------------------")
    choice = input("원하시는 간식을 골라주세요: ")  # 원하는 간식 입력
    if choice in food_list:  # 해당 간식이 리스트에 있는지 확인
        if stock_list[food_list.index(choice)] == 0:  # 리스트에는 있지만 재고가 없을 경우
            print("품절입니다. 다시 골라주세요.")
        else:
            print("%s를 골랐습니다." % choice)
            # 해당 물품의 재고를 하나 줄임
            stock_list[food_list.index(choice)] = stock_list[food_list.index(choice)] - 1
            select_list.append(choice)  # 장바구니에 하나 넣음
            # 장바구니에 넣은 물품의 갯수 추가
            select_list2[food_list.index(choice)] = select_list2[food_list.index(choice)] + 1
            full_price = full_price + price_list[food_list.index(choice)]
            more = input("더 필요하신것은 없습니까? (네/더 필요) >> ")  # 더 고르고 싶은지 물어봄
            if more == "더 필요":  # 더 고르고 싶으면 다시
                continue
            while more != "더 필요" and more != "네":  # 네, 아니오가 아닌걸 입력했을때
                more = input("잘못 입력하셨습니다. 다시 입력해주세요. (네/더 필요) >> ")
                if more == "네":  # 네 이면 그대로 끝냄
                    break
                else:  # 둘 다 아닌경우
                    pass
            break
    else:
        print("잘못 입력하셨습니다. 다시 입력해주세요.")
# 골랐던 물품들 출력
for l in range(0, len(food_list)):
    if select_list2[l] != 0:  # 장바구니에 수량이 있을 경우에만 출력해줌
        print("%s: %d개" % (food_list[l], select_list2[l]))

print("고르신 간식들의 총액은 %d원입니다." % full_price)
while True:
    payment = input("원하시는 결제 수단을 골라주세요 (카드/현금) >> ")  # 결제 수단 입력
    if payment == "카드":
        print("결제완료")
        break
    elif payment == "현금":
        pay = int(input("현금을 넣어주세요 : "))
        # 금액이 모자라면 채워질때까지 돈을 넣음
        while pay < full_price:
            pay2 = int(input("돈을 더 넣어주세요: "))
            pay = pay + pay2
        print("넣은 금액: %d" % pay)
        print("결제완료")
        # 잔돈 계산
        change = pay - full_price
        print("잔돈은 %d원입니다." % change)
        if change >= 500:
            change_500 = change // 500
            print("500원짜리 %d개" % change_500, end=" ")
            change_100 = (change - 500 * change_500) // 100
            if change_100 != 0:
                print("100원짜리 %d개" % change_100)
        else:
            change_100 = change // 100
            print("100원짜리 %d개" % change_100)
        break
    else:
        print("잘못 입력하셨습니다. 다시 입력해주세요.")

print("\n안녕히가세요.")
