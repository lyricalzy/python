from tkinter import *


def ex01():
    print("#1")
    subject = []
    for _ in range(0, 4):
        subject.append(input("배우고 싶은 과목 입력>> "))
    print(subject)


def ex02():
    print("#2")
    original = [50, 40, 30, 20]
    plus = []
    for i in range(0, len(original)):
        plus.append(original[i] + 10)
    print("plus =", plus)


def ex03():
    print("#3")
    item = ["광고", "마케팅", "그로스해킹"]
    file = open("hongbo.txt", "w")
    for x in item:
        file.write(x + "\n")
    file.close()
    file2 = open("hongbo.txt", "r")
    for _ in range(0, 3):
        temp = file2.readline()
        data = temp.strip()
        print(data)
    file.close()


def ex04():
    print("#4")
    file3 = open("hongbo.txt", "r")
    for _ in range(0, 3):
        temp = file3.readline()
        data = temp.strip()
        print(data + "짱", end=" ")
    print()
    file3.close()


def ex05():
    print("#5")
    product = ["노트북", "갤럭시탭", "휴대폰"]
    price = [150, 130, 120]
    for j in range(0, 3):
        print("%s은 %d만원입니다." % (product[j], price[j]))
    file4 = open("product.txt", "w")
    for y in product:
        file4.write(y + "\n")
    file4.close()
    file5 = open("last_price.txt", "w")
    for z in price:
        file5.write(str(z) + "\n")
    file5.close()
    file6 = open("product.txt", "r")
    temp = []
    for _ in range(0, 3):
        temp.append(file6.readline().strip())
    file6.close()
    file7 = open("last_price.txt", "r")
    data = []
    for _ in range(0, 3):
        data.append(int(file7.readline().strip()))
    file7.close()
    for k in range(0, 3):
        print("%s은 %d만원입니다." % (temp[k], data[k] + 10))


w = Tk()
w.geometry("200x350")
button1 = Button(w, text="#1", bg="blue", font=("새 굴림", 30), fg="white", comman=ex01)
button1.pack()
button2 = Button(w, text="#2", bg="blue", font=("새 굴림", 30), fg="white", command=ex02)
button2.pack()
button3 = Button(w, text="#3", bg="blue", font=("새 굴림", 30), fg="white", command=ex03)
button3.pack()
button4 = Button(w, text="#4", bg="blue", font=("새 굴림", 30), fg="white", command=ex04)
button4.pack()
button5 = Button(w, text="#5", bg="blue", font=("새 굴림", 30), fg="white", command=ex05)
button5.pack()
w.mainloop()
