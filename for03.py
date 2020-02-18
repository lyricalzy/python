target = {1, 2, 3}
print(1 in target)  # in: 리스트에 값이 존재하면 True 반환

# x는 리스트에서 요소를 꺼내 임시 저장해두는 변수
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in ls:
    print(x, end="")
print()

# x는 리스트의 인덱스를 표현할 변수
for x in range(0, len(ls), 2):
    print(ls[x])