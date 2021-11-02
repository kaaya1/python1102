#DemoLoop.py

#계산을 해야 하는 경우
value = 5
while value > 0:
    print(value)
    value-=1

print("---두번째 연습---")

value=1
while value < 10:
    print(value)
    value+= 1

#갯수를 이미 알고 있는 경우
lst = ["apple", 100, 3.14]
print("갯수:", len(lst))
for item in lst:
    print(item, type(item))

#딕셔너리
d={"apple":100, "kiwi":200, "orange":300}
for item in d.items():
    print(item)

print("---키를 출력---")
for k in d.keys():
    print(k)

print("---키를 출력---")
for v in d.values():
    print(v)

for i in [2,3,4,5,6]:
    print("---{0}단---".format(i))
    for j in [1,2,3,4,5,6,7,8,9]:
        print("{0} * {1} = {2}".format(i, j, i*j))

#수열함수를 사용
for i in range(1,11):
    print("*"*i)


lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i > 5:
        break 
    print("item:{0}".format(i))

print("---continue---")
for i in lst:
    if i % 2 == 0:
        continue 
    print("item:{0}".format(i))

    