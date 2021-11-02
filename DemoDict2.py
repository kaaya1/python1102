#DemoDict2.py

tel = {"kim":"1111", "lee":"2222"}

phone=tel

print(tel)
print(phone)
print(tel)

#불린(bool)
isRight = True
print(type(isRight))
x=5
y=5
#s\논리식에서 비교 연산자를 사용
#중단점(Break Point, 빨간점)
print(x==y)
print(x !=y)
print( 2 >1)
print(5/2)
print(5//2)
print(5%2)  #나머지값을 구할 때

#and는 ~이고, ~이면서 
#or 연산자는 ~이거나
print(True and True and True)
print(True and True and False)
print(True or False and False)

#파이썬의 판단 근거
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("demo"))
print(bool([1,2,3]))
print(bool([]))

#얕은 복사
a = [1,2,3]
b = a[0] = 38
print(a)
print(b)
print(id(a), id(b))

print("----깊은복사----")

a = [1,2,3]
#리스트 객체 전체를 복사해 달라~~
b = a[0] = 38
print(a)
print(b)
print(id(a), id(b))

While True:
score = int(input("점수를 입력:"))
if 90 <= score <= 100:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
else:
    grade = "D"

print("등급은", grade)