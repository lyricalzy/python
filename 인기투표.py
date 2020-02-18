from tkinter import *

vote_list = []
person = []


def vote(x):
    print("인기투표 시작>>", x)
    vote_list.append(x)


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

w = Tk()
w.geometry("400x500")
for v in person:
    new_button = Button(w, text=v + " 투표", bg="blue", font=("새 굴림", 30), fg="white", command=lambda: vote(v))
    new_button.pack()
w.mainloop()

print("--------------------------------")
print("최종 결과:", end=" ")
for i in range(0, len(person)):
    print("%s(%d표)" % (person[i], vote_list.count(person[i])), end=" ")
