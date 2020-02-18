# 14
food = ["두부", "김치", "숙주", "고기", "계란"]
print(food)
print(food[0], food[-1])
print(food[2])
print(food[2:6])

# 15
print("===============================")
portal = []
portal.append("네이버")
print(portal)
portal.append("카카오")
print(portal)
portal.append("구글")
print(portal)
portal.append("링크드인")
print(portal)

# 16
print("===============================")
score = []
sum = 0
for i in range(0, 3):
    temp = int(input("학기 총점: "))
    score.append(temp)
    sum = sum + score[i]
print("--------------")
print("총학기 평균은", str(sum//3) + "점입니다.")
