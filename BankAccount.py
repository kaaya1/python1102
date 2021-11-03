# BankAccount.py

#은행의 계정을 표현한 클래스 
#파이썬의 문제점(모든 요소가 public이다~~)
class BankAccount:
    #초기화 메서드로 초기값 셋팅
    def __init__(self, id, name, balance):
        #변수명을 숨겨달라(이름변경.namemangling)
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    #입금
    def deposit(self, amount):
        self.__balance += amount 
    #출금
    def withdraw(self, amount):
        self.__balance -= amount
    #원하는 문자열을 출력
    def __str__(self):
        return "{0}, {1}, {2}".format(self.__id, 
        self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.withdraw(3000)
print(account1)
#클래스 외부(인스턴스에서) 접근이 되는가?
#print(account1.__balance)
#클래스 외부에서는 _클래스명__변수명(백도어-뒷문)
print(account1._BankAccount__balance)



