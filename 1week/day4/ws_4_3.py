# import requests
# from pprint import pprint as print

# 무작위 유저 정보 요청 경로
# API_URL = 'https://jsonplaceholder.typicode.com/users/1'
# API 요청
# response = requests.get(API_URL)
# JSON -> dict 데이터 변환
# parsed_data = response.json()

# 응답 데이터 출력
# print(response)

# 변환 데이터 출력
# print(parsed_data)

# 변환 데이터의 타입
# print(type(parsed_data))


import requests
from pprint import pprint

API_BASE_URL = 'https://jsonplaceholder.typicode.com/users/'

dummy_data = []

for user_id in range(1, 11):  
    response = requests.get(API_BASE_URL + str(user_id))
    parsed_data = response.json()
    
    # Convert lat and lng to float for comparison
    lat = float(parsed_data['address']['geo']['lat'])
    lng = float(parsed_data['address']['geo']['lng'])
    
    user_info = [parsed_data['company']['name'], lat, lng, parsed_data['name']]
    
    if lat >= 80 or lng <= -80:
        # Skip this user and move to the next iteration of the loop
        continue

    dummy_data.append(user_info)

pprint(dummy_data)







