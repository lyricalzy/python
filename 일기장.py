# 일기 : 날짜, 제목, 날씨, 내용
# 파일이름 : 날짜.txt, 위치는 exercise아래로(default)
# 일기를 쓸 때마다 날짜가 다르다 = 파일이름이 달라진다.

if (input('id: ') == "root" and input("pw: ") == "1234"):
    day = input("오늘의 날짜: ")
    title = input("오늘의 제목: ")
    weather = input("오늘의 날씨: ")
    content = input("오늘의 내용: ")
    diary = open(day + '.txt', "w")
    diary.write(day + "\n")
    diary.write(title + "\n")
    diary.write(weather + "\n")
    diary.write(content + "\n")
else:
    print("아이디와 패스워드가 맞지 않습니다.")
