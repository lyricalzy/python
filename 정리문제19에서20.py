# 19
me = {"이름": "박재영", "키": "173", "나이": "28", "몸무게": "80", "가족": "장남"}
print(me.get("키"))

# 20
print("===========================")
place = []
while True:
    temp = input("장소(종료 x): ")
    if (temp == "x" or temp == "X"):
        break
    place.append(temp)
print("----------------------")
print(place)
for x in place:
    if x == "강남":
        for j in range(0, len(place)):
            if place[j] == "강남":
                break
        del (place[j])
print(place)
for y in place:
    if y == "제주도":
        for k in range(0, len(place)):
            if place[k] == "제주도":
                break
        place[k] = "제주시"
print(place)
for l in range(1, len(place) + 1):
    print(str(l) + "위:", place[l - 1])
