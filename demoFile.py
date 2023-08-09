# demoFile.py 
#파일 쓰기(유니코드로 쓰기와 읽기: utf-8)
f = open("c:\\work\\demo.txt", "wt", encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close() 

#파일 읽기(raw string notation) 
f = open(r"c:\work\demo.txt", "rt", encoding="utf-8")
print(f.read())
print("---readline()---")
f.seek(0)
#코드에서 보정 
print(f.readline(), end="")
print(f.readline(), end="")
print("---readlines()---")
f.seek(0)
result = f.readlines() 
print(result)
for item in result:
    print(item, end="")

f.close() 

