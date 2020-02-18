import datetime
# hour = int(input("지금 시각은? >> "))
now = datetime.datetime.now()
print("현재는", now)
hour = now.hour
print("현재 시각은", str(hour) + "시")
if hour <= 11:
    print("굿모닝")
elif hour <= 17:
    print("굿애프터눈")
elif hour <= 22:
    print("굿이브닝")
else:
    print("굿나잇")
print("-------------------------")
print("올해는", str(now.year) + "년")
print("현재 달은", str(now.month) + "월")
print("오늘은", str(now.day) + "일")