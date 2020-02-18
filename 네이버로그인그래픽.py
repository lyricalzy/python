from tkinter import *  # alt + Enter = 자동 import
from tkinter.messagebox import *


# 함수 = function(기능)
def login2():  # 특정한 객체에 함수를 연결(bind)
    print("login2함수 호출됨.")
    # 1. 입력한 id, pw를 가지고 온다.
    id = id_text.get()
    pw = pw_text.get()

    # 2. 입력한 id에 해당하는 파일을 읽기 전용으로 stream을 만든다.
    file_name = id + ".txt"
    file = open(file_name, "r")

    # 3. 파일에서 id, pw를 차례대로 읽어온다음, stream을 닫아준다.
    id_saved = file.readline()
    pw_saved = file.readline()
    file.close()

    # 4. 읽어온 후, 비교하기 전에 데이터에 문제가 있으면 미리 처리해줘야함.(전처리)
    id_saved2 = id_saved.strip() # 공백을 없애주는 함수
    pw_saved2 = pw_saved.strip()

    # 5. 비교 처리 하여 결과 출력
    if (id == id_saved2 and pw == pw_saved2):
        showinfo("결과", "로그인 ok..")
    else:
        showinfo("결과", "로그인 not..")

def login():
    print("login함수 호출됨.")
    id = id_text.get()  # get(): 어딘가에 들어가 있는 값을 가져옴
    pw = pw_text.get()
    if id == "root" and pw == "1234":
        showinfo("결과", "로그인 ok..")
    else:
        showinfo("결과", "로그인 not..")


w = Tk()  # 창을 만들어줌
w.geometry("500x400")  # 가로 500 세로 400 크기의 창

w.config(bg="lime")  # 배경색
id_label = Label(w, text="사용자 ID입력", font=("맑은고딕", 30), bg="lime", fg="blue")  # 아이디 라벨
id_label.pack()  # default는 가운데

id_text = Entry(w, font=("맑은 고딕", 30), bg="yellow", fg="red")  # 아이디 입력 라벨
id_text.pack()

pw_label = Label(w, text="사용자 PW입력", font=("맑은고딕", 30), bg="lime", fg="blue")  # 패스워드 라벨
pw_label.pack()  # pack : 포장하다

pw_text = Entry(w, font=("맑은 고딕", 30), bg="yellow", fg="red")  # 패스워드 입력 라벨
pw_text.pack()

# button = Button(w, text="me")
icon = PhotoImage(file="naver_login.png")  # 이미지로 부품화(객체화) 시켜줌
button = Button(w, image=icon, command=login2)  # 처리하는 login 함수를 만들어줘야 함
button.pack()

w.mainloop()  # 계속 화면에 떠있게 하는 함수
# . : 접근 연산자
