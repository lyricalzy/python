# 10
for i in range(1, 21):
    print(i)
for j in range(1, 21):
    print(j, end=" ")
print()

# 11
print("====================")
for k in range(2, 51, 2):
    print(k, end=" ")
print()

# 12
print("====================")
count = 0
for l in range(1, 1000):
    if l % 3 == 0:
        count = count + 1
    else:
        pass
print(count)

# 13
print("====================")
while True:
    food = input("먹고 싶은 음식 입력(종료: x) : ")
    if (food == "x" or food == "X"):
        break
print("---------------------------------")
print("입력을 종료합니다.")
