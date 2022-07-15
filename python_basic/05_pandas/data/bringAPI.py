# 모듈 import
import requests
import pprint

#인증키 입력
encoding = 'jfPDHbPykrBGk6BX0QAmXU01mhVSRUB73i8GosFRkPBx06ScPZ7uI2EK0zgtuMnM6p%2BB%2BI4BdVbPu53%2BG0i39A%3D%3D'
decoding = 'jfPDHbPykrBGk6BX0QAmXU01mhVSRUB73i8GosFRkPBx06ScPZ7uI2EK0zgtuMnM6p+B+I4BdVbPu53+G0i39A=='

#url 입력
url = 'http://apis.data.go.kr/1611000/AptAccnutReportService/getAccnutReportList'
params ={'serviceKey' : decoding , 
'resultCode' : '	00', 
'resultMsg' : 'NORMAL SERVICE', 
'kaptAddr' : '부산광역시 사하구 괴정동 258', 
'doroJuso' : '부산광역시 사하구 낙동대로 180', 
'kaptCode' : 'A10027875',
'kaptName' : '괴정 경성스마트W아파트',
'audtYear' : '2014'
}

response = requests.get(url, params=params)

# xml 내용
content = response.text

# 깔끔한 출력 위한 코드
pp = pprint.PrettyPrinter(indent=4)
#print(pp.pprint(content))

# Python3 샘플 코드 #


#import requests

#url = 'http://apis.data.go.kr/1611000/AptAccnutReportService/getAccnutReportList'
#params ={'serviceKey' : '서비스키', 'bjdCode' : '26380', 'pageNo' : '1', 'numOfRows' : '10' }

#response = requests.get(url, params=params)
#print(response.content)