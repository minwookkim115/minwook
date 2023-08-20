black_list = ['Hoeger LLC', 'Keebler LLC', 'Yost and Sons', 'Johns Group', 'Romaguera-Crona']

import requests
from pprint import pprint as print

dummy_data = []

for i in range(1, 11):
# 무작위 유저 정보 요청 경로
    API_URL = f"https://jsonplaceholder.typicode.com/users/{i}"

# API 요청
    response = requests.get(API_URL)
# JSON -> dict 데이터 변환
    parsed_data = response.json()
    
    my_dict = {}
    my_dict["company"] = parsed_data["company"]["name"]
    my_dict["lat"] = parsed_data["address"]["geo"]["lat"]
    my_dict["lng"] = parsed_data["address"]["geo"]["lng"]
    my_dict["name"] = parsed_data["name"]

    if -80 < float(my_dict.get("lat")) < 80 and -80 < float(my_dict.get("lng")) < 80:
        dummy_data.append(my_dict)

# print(dummy_data)


def create_user(data):
    censored_user_list = {}

    for user in data:
        if censorship(user) == True:
            new_dict = {user["company"] : [user["name"]]}
    
            censored_user_list.update(new_dict)

    return censored_user_list
    

        # user의 회사 정보를 확인해서 user의 회사가 블랙리스트에 있다면... 리스트에 추가 xxx
        # 블랙리스트에 없다면 추가

def censorship(user):
    # 유저의 회사명이 블랙 리스트 안에 있는지 판단
    if user["company"] in black_list:
        print(f"{user['company']} 소속의 {user['name']}은/는 등록할수 없습니다.")
        # 블랙리스트 안에 있다면 False 리턴
        return False
    else:
        # 블랙리스트 안에 없다면 True 리턴
        print("이상 없습니다.")
        return True
    

print(create_user(dummy_data))