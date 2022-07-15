import urllib.request
#urllib - URL처리 모듈
#urllib.request - url을 읽고 열기위한 확장 가능한 라이브러리

# url = '이미지 url 주소'
# savename = 'test.png'

# urllib.request.urlretrieve(url,savename)

# from urllib import request
url = 'https://www.naver.com/'
# mem = request.urlopen(url).read()
# print(mem.decode('utf-8')) #한글이 깨져서 나오는거 처리

import requests
# r = requests.get(url)
# print(r.text)
r = requests.get('https://api.github.com/user', auth=('user','pass'))
print(r.status_code)
print(r.encoding)
print(r.json())