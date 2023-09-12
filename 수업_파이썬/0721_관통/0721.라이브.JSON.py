import json # 내장 모듈

# json 데이터
json_data = '''
{
    "name" : "김싸피",
    "age" : 28,
    "hobbies" : [
        "공부하기",
        "복습하기"
    ]
}
'''

# print(json_data['age']) # 문자열이기 때문에 접근 불가능

# json.loads => 문자열의 json 데이터를 dict으로 변환하는 함수
data = json.loads(json_data)
print(data)

print(type(data))

# json 데이터에서 원하는 데이터만 가져오기
name = data.get("name")
name1 = data["age"]

print(name, name1)