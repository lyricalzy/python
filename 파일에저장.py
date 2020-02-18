movies = ["정직한 후보", "작은 아씨들", "클로젯", "기생충", "수퍼소닉"]

for data in movies:
    print(data)
print("----------------------------------")

for index in range(0, len(movies)):
    print(movies[index])

# 리스트, 딕셔너리 : collection 계열 내용 확인
print(movies)

file = open("movie.txt", "w")  # 강물(steam)을 연다.
# finance.naver.com site로 연결
# 사이트, 네트워크, 데이터베이스, 파일연결 등 외부 자원 연결
# => stream을 만들어야 한다.

# file.write("내용이 들어갑니다.")
for data2 in movies:
    file.write(data2 + "\n")
