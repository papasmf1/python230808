# class1.py 
#1)클래스(형식) 정의
class Person:
    #초기화 메서드
    def __init__(self):
        #인스턴스 멤버 변수 초기화
        self.name = "default name"
    def print(self):
        print("My name is {0}".format(self.name))

#2)인스턴스 생성
p1 = Person() 
p1.name = "전우치"
p2 = Person() 
#3)메서드 호출
p1.print() 
p2.print() 

#런타임(실행시간)에 변수 추가
Person.title = "new title"
Person.title2 = "2번째 타이틀"
Person.titles = "3번째 타이틀"
print(p1.title)
print(p2.title2)
print(Person.titles)
