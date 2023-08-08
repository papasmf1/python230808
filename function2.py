# function2.py 
#변수명 해석(LGB)
x = 1       #전역 변수 
def func1(a):
    return a+x 

#호출
print(func1(1))

def func2(a):
    x = 5   #지역 변수 
    return a+x 

#호출
print(func2(1))

#기본값 함수 
def times(a=10, b=20):
    return a*b 

#호출
print(times())
print(times(5))
print(times(5,6))

#키워드 인자방식
def connectURI(server, port):
    strURL = "https://" + server + ":" + port 
    return strURL 

#호출
print(connectURI("ycampus.co.kr", "80"))
print(connectURI(port="8080", server="ycampus.co.kr"))

#가변인자(인자 갯수 자유롭다)
def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result 

#호출(디버깅시에 중단점)
print(union("HAM","EGG"))
print(union("HAM","EGG","SPAM"))

#람다(이름이 없는 일회성 함수)
g = lambda x,y:x*y
print( g(3,4) )
print( (lambda a:a*a)(3) )
print( globals() )
