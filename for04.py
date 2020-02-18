list2 = [100, 200, 300, 400, 500, 600, 700, 800, 900]
# for문을 사용하세요
# 1. 전체목록을 프린트
for i in list2:
    print(i, end=" ")
print()

# 2. 홀수 번째에 있는 요소들을 프린트
print("----------------------------------")
for j in range(0, len(list2), 2):
    print(list2[j], end=" ")
print()

# 3. 홀수 번째에 있는 요소들을 다 더해서 프린트
print("----------------------------------")
sum = 0
for k in range(0, len(list2), 2):
    sum = sum + list2[k]
print(sum)

# 4. 짝수 번째에 있는 요소들을 프린트
print("----------------------------------")
for l in range(1, len(list2), 2):
    print(list2[l], end=" ")
print()

##################################################
# for문을 이용해서 풀어보세요.
# 1부터 1000까지 더해보세요.
print("----------------------------------")
sum2 = 0
for m in range(1, 1001):
    sum2 = sum2 + m
print(sum2)