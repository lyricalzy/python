from tkinter import messagebox

name = input("짝의 이름은 무엇입니까? ")
interest = input("짝의 관심사는 무엇입니까? ")
messagebox.showinfo("확인", name + ", " + interest)

if interest == "파이썬":
    messagebox.showinfo("결과", "프로그래머가 되실 거군요")
else:
    messagebox.showinfo("결과", "데이터 분석가가 되실 거군요")

result = messagebox.askquestion("확인", "파이썬이 확실한가요?")
if result == "yes":
    messagebox.showinfo("", "열심히 하세요!")
else:
    messagebox.showinfo("", "그럼 생각중이시군요!")