import requests
# 공공 데이터 API 활용 실습 (대기오염정보)

# 1. 필요한 라이브러리 impor 하기

# 2. API URL 및 KEY 값 확인

# 3. 요청 및 응답값 확인

#4. 최종 출력 문자열
#'__의 미세먼지 농도는 __입니다. (측정소:___)'

key = 'SX4%2BNhnh5roVUuhTysQjXGOOW27422y%2BQ5Ug26waZlGAfilWbnrOo5KnZZLk4KofiqR%2FKUGv%2BiaNG5g2XIviLQ%3D%3D'

url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&sidoName=광주&returnType=json'

data1 = requests.get(url).json()

name = data1['response']['body']['items'][1]['stationName']
value = data1['response']['body']['items'][1]['pm10Value']
sidoName = data1['response']['body']['items'][1]['sidoName']
text = f'{sidoName} {name}의 미세먼지 농도는 {value}입니다.'


#5. 자신에게 텔레그램 메시지 전송 (sendMessage)

token = ''
chat_id = ''

telegram_url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'

requests.get(telegram_url)

