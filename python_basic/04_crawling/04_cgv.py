import urllib.request
from bs4 import BeautifulSoup
import requests

url = 'http://www.cgv.co.kr/movies/'
#res = urllib.request.urlopen(url)

res = requests.get(url).text
soup = BeautifulSoup(res,'lxml') #lxml은 파서를 의미. BeautifulSoup 생성자에서 res를 파싱하고 그 결과를 BeautifulSoup 객체로 반환한다.
# print(soup.prettify()) #prettify 함수는 BeautifulSoup 에서 파싱 처리한 파서 트리를 유니코드 형태로 리턴하는 함수
result = soup.select('strong.title')
print(result)
name = []
for item in result:
    name.append(item.text)
print(name)

result = soup.select('span.thumb-image img')
#print(result)
for item in result:
    #print(type(item))
    img.append(item['src'])
print(img)
print(list(zip(name,img)))



