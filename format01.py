import math

name = "홍길동"
age = 100.222
print(int(age))
print(math.floor(age)) # floor는 버림함수
print(round(age, 1)) #age를 소숫점 첫째자리까지 반올림
print("나의 이름은 %s이다" % name) # %s는 string 타입
print("나의 나이는 %d살이다" % age) # %d는 10진수
print("나의 이름은 %s이고 나이는 %d살이다" % (name, age))
print("나의 이름은 {0}이고 나이는 {1:0.1f}".format(name, age)) # {1:0.1f} : 소숫점 아래 1자리까지 출력