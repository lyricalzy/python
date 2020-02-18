import datetime
now = datetime.datetime.now()
month = now.month

if month < 2:
    print("아직은 조금 춥겠군요.")
elif month == 2:
    print("조금 있으면 봄이 오겠군요.")
else:
    print("새해의 시작이 되겠군요.")

if (month >= 3 and month <=5):
    print("봄입니다.")
elif (month >= 6 and month <= 8):
    print("여름입니다.")
elif (month >=9 and month <= 11):
    print("가을입니다.")
else:
    print("겨울입니다.")

if month == 2:
    print("28일이나 29일까지입니다.")
elif (month == 4 or month == 6 or month == 9 or month == 11):
    print("30일까지입니다.")
else:
    print("31일까지입니다.")