jumsu = [] #빈 리스트
i = 0
sum = 0
while i < 3:
    data = input("점수 입력>> ")
    jumsu.append(int(data))
    sum = sum + jumsu[i]
    i = i + 1

print(jumsu)
print("합계:", sum)
print("평균", sum/i)
print(jumsu.count(70)) #70이 리스트에 몇 개나 들어있는가
jumsu.sort() #리스트를 오름차순으로 정리
             #파괴적 함수(원본을 변경함)
print(jumsu) #비파괴적 함수(원본을 변경하지 않음)