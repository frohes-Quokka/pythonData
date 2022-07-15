import urllib.request
import urllib.parse #parse는 기본적으로 영어나 숫자는 전처리를 할 필요가없는데, 

url='https://search.naver.com/search.naver'
values = {
    'where':'nexearch',
    'sm':'top_hty',
    'fbm':'1',
    'ie': 'utf8',
    'query': '여름바다'
}
param=urllib.parse.urlencode(values)
url = url + '?' + param
print(url)

data = urllib.request.urlopen(url).read().decode('utf-8')
print(data)
