# 7
mis = input("미사일 이름은: ")
start = int(input("미사일 시작값은: "))
move = float(input("미사일 움직이는 값은: "))
print("--------------------------------")
print(mis + "미사일이", str(start+move) + "로 이동되었습니다.")

# 8
print("======================================")
money = int(input("받은 돈: "))
price = int(input("상품의 총액: "))
print("부가세:", price//10)
print("잔돈:", money-price)

# 9
print("======================================")
for i in range(0, 1000):
    print("★")
