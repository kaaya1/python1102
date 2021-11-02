#DemoTuple.py
tp=(1,2,3)
print(type(tp))
print(len(tp))
print(tp[1])
#함수를 정의
def calc(a,b):
    return a+b, a*b

#함수를 호출
result = calc(3,4)
print(result)


print("id: %s, name: %s" % ("kim", "김유신")))

#한번에 묶어서 입력 데이터 전달
args = (5,6)
print( calc(*args))

#형식을 변환
a = set((1,2,3))
print(a)
print( type(a))
b=list(a)
print(b)
b.append(4)
print(type(b))