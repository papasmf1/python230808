# ifelse.py 
#선택한 블럭 주석 처리: ctrl + / 
# score = int(input("점수를 입력:"))
# if 90 <= score <= 100:
#     grade = "A"
# elif 80 <= score < 90:
#     grade = "B"
# elif 70 <= score < 80:
#     grade = "C"
# else:
#     grade = "F"

# print("등급은 ", grade)

value = 5 
while value > 0:
    print(value)
    value -= 1 

lst = ['문자열', 100, 3.14]
for item in lst:
    print(item, type(item))

print("---break구문---")
lst = list(range(1,11))
print(lst)
for i in lst:
    if i > 6:
        break 
    print("Item:{0}".format(i))

print("---continue구문---")
lst = list(range(1,11))
for i in lst:
    if i % 2 == 0:
        continue
    print("Item:{0}".format(i))

#수열함수 
for i in range(10):
    print(i)

print("---수열함수---")
print(list(range(2000,2024)))
print(list(range(1,32)))
print(list(range(1,101,2)))

print("---리스트컴프리핸션---")
lst = list(range(1,11))
print([i**2 for i in lst if i > 5])
tp = ("apple", "orange", "kiwi")
print([len(i) for i in tp])

