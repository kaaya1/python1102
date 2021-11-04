#DemoRE.py

import re

#찾았으면 매칭 객체 리턴
result = re.search("[0-9]*th", "35th")
print( result)
print( result.group())

#match 함수, search 함수 비교
#match 함수는 정확하게 일치
#search 함수는 포함하고 있을때
print( bool(re.match("ap", "this is apple")))
print( bool(re.search("ap", "this is apple")))
