import requests


name = input()

url = f'https://api.nationalize.io/?name={name}'

response = requests.get(url).json()

name = response['name']
country = response['country'][0]['country_id']
p = round((response['country'][0]['probability'])*100,2)
print(f'{name}님의 국적은 {p}% 확률로 {country}.')


