# web2.py 
#웹서버 실행 요청 
import requests
#웹크롤링 
from bs4 import BeautifulSoup

url = "https://www.daangn.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

#파일 저장
f = open("daangn.txt", "wt", encoding="utf-8")
posts = soup.find_all("div", attrs={"class":"card-desc"})
for post in posts:
    titleElem = post.find("h2", attrs={"class":"card-title"})
    title = titleElem.text.replace("\n", "") 
    priceElem = post.find("div", attrs={"class":"card-price"})
    price = priceElem.text.replace("\n", "")  
    addrElem = post.find("div", attrs={"class":"card-region-name"})
    addr = addrElem.text.replace("\n", "")  
    print("{0}, {1}, {2}".format(title, price, addr))
    #python 3.8이상에서 사용 
    f.write(f"{title}, {price}, {addr}\n")

f.close() 

# <div class="card-desc">
#       <h2 class="card-title">전자드럼 팔아요</h2>
#       <div class="card-price ">
#         50,000원
#       </div>
#       <div class="card-region-name">
#         전북 전주시 덕진구 송천동2가
#       </div>