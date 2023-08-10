# web1.py 
#웹크롤링 코드 
#from 패키지 import 모듈명
from bs4 import BeautifulSoup

#파일을 읽어서 문자열 변수에 로딩
#메서드체인(함수체인)
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read() 
#검색이 용이한 객체 생성
#인터넷상에서 검색(html.parser, html5, xml)
soup = BeautifulSoup(page, "html.parser")
#전체를 보여달라
#print(soup.prettify())
#<p>를 몽땅 검색 
#print( soup.find_all("p") )
#첫번째 <p>만 검색
#print(soup.find("p"))
#조건으로 검색: <p class='outer-text'>
#print(soup.find_all("p", class_ = "outer-text"))
#attrs는 attributes의 약자, 딕셔너리로 전달 
#print( soup.find_all("p", attrs={"class":"outer-text"}) )
#id속성으로 검색 
#print( soup.find_all(id="first") )
#이번에는 태그 내부에 컨텐츠를 추출 
for tag in soup.find_all("p"):
    #내부 문자열을 추출 
    title = tag.text.strip() 
    title = title.replace("\n", "")
    print(title)


