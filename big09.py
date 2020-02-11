data1 = input("1년 만기 정기 예금을 얼마나 예치하시겠습니까? ")
num1 = int(data1)
num2 = num1//10
print("원금이 " + data1 + "이시군요.!")
print("이자는 " + str(num2) + "입니다.")
print("원리합계는 "+ str(num1+num2) +"입니다.")