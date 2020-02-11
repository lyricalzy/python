# 네이버 로그인
# 판단을 할 때 조건을 가지고 판단을 한다.
# 조건이 하나가 아닌 경우 논리적으로 어떻게 판단할 것인가?
# 지하철을 타는 이유 1) 편해서 2) 저렴해서
# 조건들이 모두 맞아야(all True) 논리적으로 판단하는 경우 => and조건(and)
# 조건들 중에 하나만 맞아도(one True) 논리적으로 판단하는 경우 => or조건(or)
# and와 or를 논리연산자라고 부른다.
id = "root"
pw = "pass"

id2 = input("아이디 입력: ") #admin
pw2 = input("패스워드 입력: ") #pass

if (id == id2 and pw == pw2):
    print("로그인 ok")
else:
    print("로그인 not")