hobby = ["달리기", "자전거 타기", "여행하기"]
#제 취미의 개수를 프린트해주세요.
print(len(hobby))
#제 취미가 자전거 타기에서 오토바이 타기로 변경해주세요.
# i = 0
# while i < len(hobby):
#     if hobby[i] == "자전거 타기":
#         hobby[i] = "오토바이 타기"
#     i = i + 1
hobby[1] = "오토바이 타기"
#제 취미의 전체 리스트를 프린트
print(hobby)
i = 0
while i < len(hobby):
    print(hobby[i])
    i = i + 1

del(hobby[0])
print(hobby)