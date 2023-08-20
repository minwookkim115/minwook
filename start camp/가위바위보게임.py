user = input("가위! 바위! 보!") # 입력 받기

print (f"나 : {user}")
##com = 컴퓨터가 낼 가위바위보중 하나 (할때마다 바뀐다)

# 조건문을 사용해서
# 누가 이겼는지 판별한 후에
# 승자를 출력
# 게임의 결과도 출력
# ex) 내가 가위를 내고 컴퓨터가 바위를 내서 패배하였습니다.
# ex) 내가 가위를 내고 컴퓨터가 보를 내서 승리하였습니다.

import random

l = ["가위" , "바위" , "보"]

com = (random.choice(l))

print(com)

if user == "가위" and com == "가위":
    print("내가 가위를 내고 컴퓨터가 가위를 내서 비겼습니다.")
elif user == "가위" and com == "바위":
    print("내가 가위를 내고 컴퓨터가 바위를 내서 졌습니다.")
elif user == "가위" and com == "보":
    print("내가 가위를 내고 컴퓨터가 보를 내서 이겼습니다.")
elif user == "바위" and com == "가위":
    print("내가 바위를 내고 컴퓨터가 가위를 내서 이겼습니다.")
elif user == "바위" and com == "바위":
    print("내가 바위를 내고 컴퓨터가 바위를 내서 비겼습니다.")
elif user == "바위" and com == "보":
    print("내가 바위를 내고 컴퓨터가 보를 내서 졌습니다.")
elif user == "보" and com == "가위":
    print("내가 보를 내고 컴퓨터가 가위를 내서 졌습니다.")
elif user == "보" and com == "바위":
    print("내가 보를 내고 컴퓨터가 바위를 내서 이겼습니다.")
elif user == "보" and com == "보":
    print("내가 보를 내고 컴퓨터가 보를 내서 비겼습니다.")