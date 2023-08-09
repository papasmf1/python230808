# demoOS.py 
import random

print(random.random())
print(random.random())
print(random.sample(range(20), 10))
print(random.sample(range(20), 10))
print(random.sample(range(20), 10))
lotto = list(range(1,46))
print(lotto)
random.shuffle(lotto)
print(lotto)

from os.path import * 
from os import * 

print(abspath("python.exe"))
print(basename("c:\\python310\\python.exe"))

if exists("c:\\python310\\python.exe"):
    print("파일크기:{0}".format(getsize("c:\\python310\\python.exe")))
else:
    print("파일이 없습니다.")

#특정 파일 실행
#system("notepad.exe")
print("운영체제이름:{0}".format(name))
print(environ)

import glob 
result = glob.glob("c:\\work\\*.py")
for item in result:
    print(item)

    

