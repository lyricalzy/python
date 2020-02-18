from tkinter import *
from tkinter.messagebox import *


def insert():
    print("회원가입 처리")
    # 입력값 가져옴
    id = id_text.get()
    pw = pw_text.get()
    name = name_text.get()
    tel = tel_text.get()
    # 가져온 값으로 파일 생성해서 저장
    insert_file = open(id + ".txt", "w")
    insert_file.write(id + "\n")
    insert_file.write(pw + "\n")
    insert_file.write(name + "\n")
    insert_file.write(tel + "\n")
    insert_file.close()  # stream을 닫아주어야 한다.
    showinfo("결과", "회원가입 완료")


w = Tk()
w.geometry("430x520")

w.config(bg="white")  # 배경색
icon = PhotoImage(file="naver_main.png")
naver_label = Label(w, image=icon)
naver_label.pack()
id_label = Label(w, text="아이디 입력", font=("궁서체", 30), bg="white", fg="blue")  # 아이디 라벨
id_label.pack()
id_text = Entry(w, font=("궁서체", 30), bg="yellow", fg="red")  # 아이디 입력 라벨
id_text.pack()
pw_label = Label(w, text="패스워드 입력", font=("궁서체", 30), bg="white", fg="blue")  # 패스워드 라벨
pw_label.pack()
pw_text = Entry(w, font=("궁서체", 30), bg="yellow", fg="red")  # 패스워드 입력 라벨
pw_text.pack()
name_label = Label(w, text="이름 입력", font=("궁서체", 30), bg="white", fg="blue")  # 이름 라벨
name_label.pack()
name_text = Entry(w, font=("궁서체", 30), bg="yellow", fg="red")  # 이름 입력 라벨
name_text.pack()
tel_label = Label(w, text="전화번호 입력", font=("궁서체", 30), bg="white", fg="blue")  # 전화번호 라벨
tel_label.pack()
tel_text = Entry(w, font=("궁서체", 30), bg="yellow", fg="red")  # 전화번호 입력 라벨
tel_text.pack()
button = Button(w, text="회원가입처리", bg="pink", font=("궁서체", 30), fg="blue", command=insert)
button.pack()
w.mainloop()
