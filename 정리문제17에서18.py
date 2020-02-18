# 17
answer = 77
while True:
    guess = int(input("당신이 생각한 정답 입력: "))
    if guess == 77:
        print("정답입니다.")
        break
    else:
        print("정답이 아닙니다.")

# 18
print("==========================")
data1 = int(input("입금액: "))
data2 = float(input("이자율: "))
iza = data1*0.2
print("----------------")
print("1년 후 받게 될 금액은:", str(int(data1+iza)) + "원")
