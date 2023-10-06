import matplotlib.pyplot as plt

# x축은 동일하게 맞춰주는게 좋다
# why? 축이 달라져서 원하는대로 안나올 수도 있기 때문에

# # 예제1: x, y 가 같을 때
# plt.plot([1, 2, 3, 4]) # plot => 그래프를 그려준다
# plt.show()

# # 참고: 이때까지 그렸던 plot 지우기
# plt.clf()

# 예제2: x, y 가 다를 때
x = [1, 2, 3, 4]
y = [2, 4, 8, 16]
plt.plot(x, y)
# plt.show()
# plt.clf()

# 예제3: 제목 + 각 축의 설명
plt.plot(x, y)
# 제목 => 한글은 따로 설정 해야함
plt.title("Test Graph")

# x, y 축
plt.ylabel('y label')
plt.xlabel('x label')
# plt.show()

# 파일로 저장하기 => show 지우고 해야함
plt.savefig('filename.png')