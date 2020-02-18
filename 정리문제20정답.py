# 5번 입력을 받자
location = []
# print(0 in range(0, 5))
for x in range(0, 5):
    location.append(input("장소: "))
print(location)

if ("강남" in location):
    print("강남 있음")
    # del()을 사용하려면 index가 필요
    # index = location.index("강남")
    # del location[index]
    location.remove("강남")
    print("강남을 삭제했습니다.")
    print(location)

for y in range(0, len(location)):
    if (location[y] == "강남"):
        del location[y]
        print("강남을 삭제했습니다.")
        print(location)
        break

# if ("제주도" in location):
#     print("제주도 있음")
#     index2 = location.index("제주도")
#     location[index2] = "제주시"

for z in range(0, len(location)):
    if (location[z] == "제주도"):
        print("제주도 있음")
        location[z] = "제주시"
        print("제주도를 제주시로 변경했습니다.")
        print(location)

for i in range(0, len(location)):
    print("%d위 : %s" % (i+1, location))
