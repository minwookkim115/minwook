############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum, min, max, len 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def get_row_col_maxsum(matrix):
    pass
    # row_sum = 0
    # row_sum_list = []

    # for i in matrix:
    #     for j in i:
    #         row_sum += j

    # col_sum = 0

    # for i in matrix:
    #         if i.index() == 0:
    #             col_sum += i


    # return col_sum
    
    row_len = 0 # 행 길이
    col_len = 0 # 열 길이

    # 행 ==> 리스트 안에 리스트가 몇개?
    for r in matrix:
        row_len += 1
    
    # 열 ==> 리스트 안에 리스트가 있는데 그 리스트의 원소 갯수가 몇개?
    for c in matrix[0]:
        col_len += 1

    # 가로 합


    # 세로 합



# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    example_matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    example_matrix2 = [
        [11, 5, 49, 20],
        [28, 16, 20, 33],
        [63, 17, 1, 15]
    ]
    print(get_row_col_maxsum(example_matrix))   # => ('row', 58)
    print(get_row_col_maxsum(example_matrix2))  # => ('col', 102)

    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    