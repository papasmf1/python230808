# db1.py 
import sqlite3

#연결객체(물리적인 파일에 저장) 
con = sqlite3.connect("c:\\work\\sample.db")
#커서객체 
cur = con.cursor() 
#테이블 구조 생성
cur.execute("""create table if not exists PhoneBook
    (id integer primary key autoincrement, name text, 
    phoneNum text);""")
#1건입력 
cur.execute("insert into PhoneBook (name, phoneNum) values ('홍길동','010-222');")
#입력 파라메터 처리 
name = "이순신"
phoneNumber = "010-123-1234"
cur.execute("insert into PhoneBook (name, phoneNum) values (?, ?);", 
    (name, phoneNumber))
#다중의 레코드(행) 입력 
datalist = (("전우치","010-456"),("김길동","010-7890"))
cur.executemany("insert into PhoneBook (name, phoneNum) values (?, ?);", 
    datalist)
#검색 
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)

#커밋
con.commit() 

