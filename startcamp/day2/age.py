# api 연습

import requests

# API 요청 URL 확인 + 필요한 데이터 건네주기

# name = input()

name = 'david'

url = f'https://api.agify.io/?name={name}'


# URL로 요청 보내기
response = requests.get(url).json()

# 응답결과 확인 후 정보 추출하기
name = response['name']
age = response['age']
print(f'{name}님의 예상 나이는 {age}살 입니다.')

# 복습할때 api.nationalize.io 로도 해보기
# 이거 해결해보기
