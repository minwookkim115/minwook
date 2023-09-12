# 서버에 데이터 요청
import requests

url = "https://fakestoreapi.com/carts"
response = requests.get(url) # .json()


print(response)

# .json()
# 내부의 데이터를 JSON형태로 변환해주는 함수