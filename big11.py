data1 = input("지금은 몇 시 입니까? ")
time = int(data1)
if time < 12:
    print("점심 전입니다.")
else:
    print("점심 후 입니다.")