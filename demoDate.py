# demoDate.py 
#네임스페이스를 생략한다는 의미 
from datetime import * 

d1 = date(2023, 8, 1)
print(d1)
d2 = date.today() 
print(d2)
print("100일을 더하면:{0}".format(d2))
d3 = timedelta(days=100)
print(d2 + d3)
d4 = datetime.now()
print(d4)

