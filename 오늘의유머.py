# coding:utf-8
from bs4 import BeautifulSoup
#requests를 라이브러리 
import urllib.request
#정규표현식(검색)
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

for n in range(1, 11):
        #오늘의 유머 베스트 게시판 
        data ='https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        #한글이 깨지는 경우는 다시 디코딩 
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        list = soup.find_all('td', attrs={'class':'subject'})
        
        #<td class='subject'>
        #<a href="/board/view.php?table=">잼버리 이젠 녹색 어머니회까지 동원</a>  

        for item in list:
                #에러 처리 코드 
                try:
                        title = item.find("a").text.strip()  
                        #print(title)
                        if (re.search('미국', title)):
                                print(title.strip())
                except:
                        pass
        
