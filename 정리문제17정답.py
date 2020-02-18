import random

target = random.randint(1, 100) # 1~99중 하나 생성
count = 0  # 초기화변수는 반복문안에 넣으면 안된다.
while True:
    think = int(input("생각한 값 입력>> "))
    count = count + 1
    if think == target:
        print("정답입니다.")
        print("%d번만에 맞췄습니다." % count)
        print("시스템을 종료합니다.")
        break
    else:
        print("오답입니다.")
        if think < target:
            print("너무 작아요!")
        if think > target:
            print("너무 커요!")
