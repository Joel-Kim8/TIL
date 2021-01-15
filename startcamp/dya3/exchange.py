import requests
import datetime
from bs4 import BeautifulSoup





url = 'https://finance.naver.com/marketindex/'


response = requests.get(url).text

soup = BeautifulSoup(response, 'html.parser')

ko = soup.select_one('#exchangeList > li:nth-child(1) > a.head.usd > div > span.value').text
now = datetime.datetime.now()


print((f'현재({now}) 원/달러 환율은 {ko} 입니다.'))