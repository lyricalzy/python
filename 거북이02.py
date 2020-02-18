import turtle

pen = turtle.Pen()
pen.color("red")
pen.shape("turtle")
while True:
    choice = input("왼쪽: left, 오른쪽: right, 종료: x>> ")
    if (choice == "x" or choice == "X"):
        print("종료합니다.")
        break
    if choice == "left":
        pen.left(45)
        pen.forward(100)
    if choice == "right":
        pen.right(45)
        pen.forward(100)
