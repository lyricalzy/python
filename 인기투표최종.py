vote_list = []
person = []

print("인기투표 시스템입니다.")
print("--------------------------------")
while True:
    person_temp = input("인기투표 대상자 입력(종료 x)>> ")
    if person_temp == "x" or person_temp == "X":
        break
    elif person_temp in person:
        print("이미 등록된 후보입니다. 다시 입력해주세요.")
    else:
        person.append(person_temp)
print("--------------------------------")
while True:
    vote_temp = input("인기 투표 시작(종료 x)>> ")
    if vote_temp == "x" or vote_temp == "X":
        break
    elif vote_temp in person:
        vote_list.append(vote_temp)
    else:
        pass
print("--------------------------------")
print("최종 결과: ", end=" ")
for i in range(0, len(person)):
    print("%s(%d표)" % (person[i], vote_list.count(person[i])), end=" ")
