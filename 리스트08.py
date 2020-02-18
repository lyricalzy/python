data = input("지금 먹고 싶은것? 물, 아메리카노, 맥주 >> ")
if data == "물":
    print("정수기")
elif data == "아메리카노":
    print("카페")
elif data == "맥주":
    pass #파이썬에서는 비워두면 안됨
else:
    print("다시 입력해주세요")