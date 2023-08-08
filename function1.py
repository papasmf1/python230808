# function1.py 
#1)함수 정의
def times(a,b):
    return a*b 

#2)호출
result = times(3,4)
print(result)

#함수정의
def setValue(newValue):
    #함수 내부의 지역변수
    x = newValue 
    print("지역변수:", x)

#호출
result = setValue(5)
print(result)

#교집합 문자를 리턴 함수 
def intersect(prelist, postlist):
    #지역변수
    result = []
    #H(0) | A(1) | M(2)
    for x in prelist:
        #만약에 x라는 글자가 postlist에 있고 x가 result에 없으면 
        if x in postlist and x not in result:
            result.append(x)
    return result 

#호출
print(intersect("HAM","SPAM"))

