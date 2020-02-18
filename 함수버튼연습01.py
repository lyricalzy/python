from tkinter import *


def file_write():
    print("저장")
    fruit = ["사과", "바나나", "배"]
    # 파일에 저장
    fruit_file = open("fruit.txt", "w")
    for x in fruit:
        fruit_file.write(x + "\n")
    fruit_file.close()


def file_write2():
    print("저장2")
    fruit2 = []
    for i in range(0, 5):
        fruit2.append(input("과일 입력: "))
    print(fruit2)
    # 파일에 저장
    # fruit_file = open("fruit.txt", "w")
    # for x in fruit:
    #     fruit_file.write(x + "\n")
    # fruit_file.close()


def file_read():
    print("읽기")
    file = open("fruit.txt", "r")
    for j in range(0,3):
        temp = file.readline()
        data = temp.strip()
        print(data)
    file.close()

w = Tk()  # 프레임을 만들어 주는 함수
w.geometry("200x150")
button1 = Button(w, text="저장", bg="green", font=("새 굴림", 30), fg="white", command=file_write)
button1.pack()
button2 = Button(w, text="읽기", bg="green", font=("새 굴림", 30), fg="white", command=file_read)
button2.pack()
w.mainloop()
