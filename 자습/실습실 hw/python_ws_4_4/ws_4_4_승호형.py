import requests

black_list = ['Hoeger LLC', 'Keebler LLC', 'Yost and Sons', 'Johns Group', 'Romaguera-Crona']

dummy_data = []

for i in range(1, 11):
    API_URL = 'https://jsonplaceholder.typicode.com/users/' + str(i)
    # API 요청
    response = requests.get(API_URL)
    # JSON -> dict 데이터 변환
    parsed_data = response.json()
    if ((-80) < float(parsed_data['address']['geo']['lat']) < 80) and ((-80) < float(parsed_data['address']['geo']['lng']) < 80):
        user_dict = {'company': parsed_data['company']['name'], 'lat': parsed_data['address']['geo']['lat'], 'lng': parsed_data['address']['geo']['lng'], 'name': parsed_data['name']}
        dummy_data.append(user_dict)


censored_user_list = {}

def create_user(data):
    for user in data:
        new_user = {user['company']: [user['name']]}
        
        censorship(new_user)

# print(dummy_data)
def censorship(x):
    # print(x.keys())
    if list(x.keys())[0] in black_list:
        print(f'{list(x.keys())[0]} 소속의 {list(x.values())[0][0]} 은/는 등록할 수 없습니다.')

    else:
        print('이상 없습니다.')
        censored_user_list.update(x)

create_user(dummy_data)
print(censored_user_list)