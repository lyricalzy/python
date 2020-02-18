food = ["라면", "커피", "아이스크림", "라떼", "팥빙수"]

#인덱싱
print(food[0])
print(food[-1]) #인덱스를 -1로 하면 맨 끝
print(food[-2])

#슬라이싱
print(food[0:2]) #0~1. 가져오고 싶은 값보다 1 증가시켜줘야함
print(food[2:5])
print(food[2:]) #생략하면 끝까지 인줄 앎
print(food[:3]) #0~2

print("----------------------------")
drink = ["물", "아메리카노", "맥주"]
all = food + drink
print(all)

print("----------------------------")
drink3 = drink * 3 #반복의 의미
print(drink3)

print("----------------------------")
drink.insert(0, "라떼") #제일 앞에 삽입. 파괴형 함수
print(drink)
print(drink.index("라떼"))