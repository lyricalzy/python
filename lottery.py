import random

# lotto = []  # 비어있는 리스트 생성
# lotto.append((random.randint(1, 45)))
# while True:  # 원하는 결과가 나올 때까지 돌림
#     temp = random.randint(1, 45) # 로또 번호 생성
#     if temp in lotto: # 기존 리스트에 해당 번호가 있는지 체크
#         print("동일한 숫자 있음")
#     else:
#         lotto.append(temp) # 없는 번호면 리스트에 넣어줌
#     if len(lotto) == 6:  # 리스트의 길이가 6개가 되면 끝
#         break
#
# print("이번주의 로또 번호: %s" % lotto)

lotto = set() # 비어있는 집합 생성
while True: # 원하는 결과가 나올 때까지 돌림
    lotto.add(random.randint(1, 15)) # 무작위 번호를 집합에 넣어줌.
    if len(lotto) == 3: # 집합의 길이가 6개가 되면 끝
        break
print(lotto)