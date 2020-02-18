jumsu = [] #점수를 넣을 빈 리스트
i = 0 #반복할 횟수와 리스트의 인덱스를 표현할 변수
sum = 0 #점수의 총합을 저장할 변수
while i < 3: #점수를 3번 입력받기 위해 3번 반복
    data = input("점수 입력: ") #점수를 입력받음
    jumsu.append(int(data)) #입력받은 점수를 정수로 변환해서 리스트에 저장
    sum = sum + jumsu[i] #점수의 총합을 저장해둠
    i = i + 1 #증감식

print(jumsu) #입력받은 점수의 리스트 출력
print("합계:", sum) #점수 합계 출력
print("평균:", sum/i) #점수 평균 출력