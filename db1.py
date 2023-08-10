# db1.py 
import sqlite3

#연결객체(일단 메모리에 저장) 
con = sqlite3.connect(":memory:")
#커서객체 
cur = con.cursor() 
#테이블 구조 생성
cur.execute("""create table if not exists PhoneBook
    (id integer primary key autoincrement, name text, 
    phoneNum text);""")
#1건입력 
cur.execute("insert into PhoneBook (name, phoneNum) values ('홍길동','010-222');")
#검색 
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)

