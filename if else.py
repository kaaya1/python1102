# ifelse.py
print("---citrl+c를 클릭 종료---")
while True:
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
