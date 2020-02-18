# 3번 반복하고 싶은 경우

# 별 10개를 한줄로
for x in range(0, 10, 3): # 3번째 숫자는 증감할 양을 정해줌.
    # print(x)
    print("★", end=" ")
print()
print("------------------------")
#이중 for문
for y in range(0, 10):
    for x in range(0, 10):
        # print(x)
        print("★", end=" ")
    print()