# test.py

print("hello python!!")
#사전식
color = {"apple":"red", "kiwi":"green"}
print(type(color))
print(len(color))
print(color["apple"])
#입력
color["cherry"] = ["red"]
#items()메서드는 키와 값을 동시에 반환
#디버깅 모드의 경우 무조건 중지(break point)
for item in color.items():
    print(item)

for k,v in color.items():
    print(k,v)
#키만 출력
for k in color.keys():
    print(k)
#값만 출력
for v in color.values():
    print(v)
