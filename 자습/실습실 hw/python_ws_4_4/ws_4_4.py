black_list = ['Hoeger LLC', 'Keebler LLC', 'Yost and Sons', 'Johns Group', 'Romaguera-Crona']

import requests
from pprint import pprint as print

dummy_data = []

for i in range(1, 11):
# 무작위 유저 정보 요청 경로
    API_URL = "https://jsonplaceholder.typicode.com/users/" + str(i)

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

print(dummy_data)

def censorship():
    
    for i in dummy_data:
        if i["company"] in black_list:
            print(f"{i['company']}소속의 {i['name']}은/는 등록할 수 없습니다.")
        else:
            print("이상 없습니다.")
            
censored_user_list = {}

def create_user():
    
    for user in dummy_data:
        if user["company"] in black_list:
            pass
        else:
            new_list = []
            new_list1 = list(user["name"])
            new_list2 = "".join(new_list1)
            new_list.append(new_list2)

            new_dict = {user["company"] : new_list}

            censored_user_list.update(new_dict)
        

censorship()
create_user()
print(censored_user_list)
