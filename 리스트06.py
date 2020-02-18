# 입력: 홍길동
# 입력: 파이썬
# 입력: 프로그래머
# 입력: 데이터 분석가

# sum이라는 변수에 입력값 누적하여 프린트
# 홍길동 파이썬 프로그래머 데이터 분석가

i = 0
sum = ""
while True:
    data = input("입력(종료는 x): ")
    # 입력된 값이 x인지를 먼저 체크해야함.
    if (data == "x" or data == "X"):
        print("프로그램을 종료합니다.")
        break #반복문을 종료
    sum = sum + data + " "

print(sum)