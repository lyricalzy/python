data1 = input("첫번째 물품의 가격을 입력해주세요: ")
data2 = input("첫번째 물품의 수량을 입력해주세요: ")
data3 = input("두번째 물품의 가격을 입력해주세요: ")
data4 = input("두번째 물품의 수량을 입력해주세요: ")

item1 = int(data1)
count_item1 = int(data2)
item2 = int(data3)
count_item2 = int(data4)
price_item1 = item1*count_item1
price_item2= item2*count_item2
full_price = price_item1 + price_item2
discount = full_price//10

vip = input("우수회원 이십니까? Y/N >> ")
if vip == "Y":
    print("우수회원은 10%할인된 가격입니다.")
    print("결제하실 금액은 " + str(full_price-discount) + "원입니다.")
else:
    print("결제하실 금액은 " + str(full_price) + "원입니다.")