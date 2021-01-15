import requests
import datetime
from bs4 import BeautifulSoup
# url = 'https://naver.com'
# response = requests.get(url).text
# print(type(response))
# #print(response)

# from bs4 import BeautifulSoup
# soup = BeautifulSoup(response)
# print(type(soup))


# 코스피 가져오기

# 요청 보낼 주소 확인
url = 'https://finance.naver.com/sise/'

# requests로 요청을 보내고 응답으로 텍스트 받기
response = requests.get(url).text

# str을 구조화하여 데이터를 추출하기 쉬운 형태로 바꾸기
soup = BeautifulSoup(response, 'html.parser')

# 경로를 건네주고 원하는 정보 추출하기
ko = soup.select_one('#KOSPI_now').text
now = datetime.datetime.now()


print((f'현재({now}) KOSPI {ko} 입니다.'))