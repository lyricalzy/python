import random

jumsu = []

random.seed(4)
for i in range(0, 10000):
    jumsu.append(random.randint(1, 1000))

print(jumsu)

# count = jumsu.count(512)
# print(count)

count2 = 0
for x in jumsu:
    if x == 455:
        count2 = count2 + 1
print(count2)

for i in range(0, len(jumsu)):
    if jumsu[i] == 455:
        print(i, end=" ")
