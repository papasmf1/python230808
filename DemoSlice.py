#DemoSlice.py 
strA = "python is very powerful"
strB = "파이썬은 강력해"
print( len(strA) )
print( len(strB) )

print( strA[0:6] )
print( strB[0:4] )
print( strA[:6] )
print( strB[:4] )
print( strA[-3:] )
print( strB[-3:] )

strC = '''다중라인을
저장해서
작업하는 경우'''
print(strC)

#대소문자 구분
friend = 5 
Friend = 6 
print(friend)
print(Friend)

#리스트 형식
colors = ["red", "blue", "green"]
print( type(colors) )
colors.append("white")
print(colors)
colors.insert(1, "pink")
print(colors)
print(colors.index("pink"))
colors += ["red"]
colors += "red"
print(colors)
print(colors.pop())
print(colors.pop())
print(colors.pop())
print(colors)
#정순으로 정렬
colors.sort()
print(colors)
#역순으로 정렬
colors.reverse()
print(colors)

print("---set형식---")
a = {1,2,3,3}
b = {3,4,4,5}
print(a)
print(type(b))
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))



