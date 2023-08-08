# DemoDict.py 
device = {"아이폰":5, "아이패드":10, "윈도우":15}
#검색
print(device["아이폰"])
#입력
device["맥북"] = 20 
#수정
device["아이폰"] = 6 
print(device)
#삭제
del device["아이패드"]
print(device)

#전화번호(참조 복사)
phone = {"kim":"1111", "lee":"2222", "park":"3333"}
print("kim" in phone)
print("kang" not in phone)
p = phone
print(p)
print(phone)
p["kang"] = "1234"
print(phone, p)
print(id(phone), id(p))

