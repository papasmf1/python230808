# DemoTuple.py 
print("---tuple형식---")
tp = (1,2,3)
print(len(tp))
print(tp[0])
print("id: %s, name: %s" % ("kim","김유신"))

#함수를 정의
def calc(a,b):
    return a+b, a*b 

#함수를 호출(디버깅할 때 중단점-Break Point)
result = calc(3,4)
print(result)
#*를 붙이면 Tuple형식이라는 뜻 
args = (5,6)
print(calc(*args))

print("---형식변환---")
a = set((1,2,3))
print(a)
b = list(a)
b.append(4)
print(b)
c = tuple(b)
print(c)

print("---dict형식---")
fruits = {"apple":"red", "banana":"yellow"}
print(fruits["apple"])
fruits["kiwi"] = "green"
print(fruits)
for item in fruits.items():
    print(item)

for k,v in fruits.items():
    print(k, v)

print("---값만 출력---")
for v in fruits.values():
    print(v)

print("---키만 출력---")
for k in fruits.keys():
    print(k)


