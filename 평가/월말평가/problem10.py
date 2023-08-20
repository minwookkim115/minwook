############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum, min, max, len 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def find_one(matrix):

  for i in matrix:
     for j in i:
        if j == 1:
           
           return (matrix.index(i), i.index(j))

  # 2차원 리스트의 길이 구하기
  row = 0 # 행 길이
  col = 0 # 열 길이
  
  # 행 길이 구한다음
  for r in matrix:
    row += 1

    
  # 행 길이 == 열 길이
  col = row

  # 1의 위치 찾기
  # 행 반복 0 <= r < row
  for row in range(row):
    # 열 반복 0 <= c < col
    for c in range(col):
       if matrix[r][c] == 1:
          return (r, c)


# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    sample_matrix = [
      [0, 0, 0],
      [0, 1, 0],
      [0, 0, 0]
    ]
    print(find_one(sample_matrix))  # => (1, 1)
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    