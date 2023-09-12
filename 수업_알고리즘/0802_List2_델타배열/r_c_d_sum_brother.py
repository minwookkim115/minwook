#구하고자 하는 것은 행들의 총합, 열들의 총합, 대각선의 총합 중 총합의 최댓값을 구하고자 한다.

#제시하는 테스트 문제의 수가 10으로 정해짐
for i in range(10): # 테스트의 양이 10으로 정해져있으므로 test case의 범위는 1~11 까지
    tc = int(input())
    n = 100   # 100*100 을 나타내는 행렬로 동일하게 기입되어 있음 따라서 n과 m의 값은 100*100 의 행렬을 나타내면 됨
    # n의 값만 지정해도 배열에서 행우선 순회로 지정하여 range(n)값을 지정해주면 m 값이 없어도 100*100 행렬을 만들어줄 수 있지 않을까?

    baeyeul = [list(map(int,input().split())) for _ in range(n)]
    max_val = 0 # 행과 열의 최댓값을 저장하기 위한 변수값 지정하기

    # 행들의 최댓값을 구하기 위한 포문작성
    # 행들의 최댓값을 구하기 위한 것이므로 변수의 순서는 [행][열]
    for r in range(100): # 행의 합들의 값을 구하기 위한 포문 작성
        sum_r = 0 # 행의 최대 값을 구하기 위해 초기값을 설정한다.
        for nr in range(100) : #행의 값을 구하기 위한 포문작성 열의 값을 구하기 위해서는 리스트에 list[r][c]
            # sum_r = baeyeul[r][nr] # = sum_r 이 그 자리에서 갖는 값을 알기위해 작성하는 식
            sum_r += baeyeul[r][nr] # sum_r 중에서 같은 r 값을 갖는 c 들의 총합 = 같은 행에 위치한 0~99까지 열의 총합
            if sum_r > max_val : # 각 행에 위치한 열의 총합이 기존에 저장된 값보다 큰지를 비교
                max_val = sum_r # 열의 총합이 기존의 합보다 크면 max_val의 값을 sum_r과 동일하게 변경하겠다.

    # 열들의 최댓값을 구하기 위한 포문 작성
    # 열들의 최댓값을 구하기 위한 것이므로 변수의 순서는 [열][행]
    for c in range(100): # 열들의 값을 구하기 위한 포문작성
        sum_c = 0 # c열 값의 총합을 구하기 위한 것이므로 초기값 설정
        for nc in range(100): #열을 이루는 행을 구하고 그 열의 행들의 총합의 값을 구하기 위한 포문
            # sum_c = baeyeul[nc][c] # => 열을 이루는 행의 해당위칫 값을 알기위해 작성
            sum_c += baeyeul[nc][c] # nc열에 위치한 행들의 총합
            if sum_c > max_val : # 행들의 총합이 현재 저장되어 있는 max_val(행을 이루는 열의 총합) 보다 큰지 비교하겠다.
                max_val = sum_c # 만약 sum_c 의 값이 max_val의 값보다 크다면 max_val의 값을 sum_c로 변경하겠다.

    # 대각선을 이루는 값들의 총합을 구하기 위한 포문 작성 (대각선을 영어로 다이아 고날(diagonal)이란 것을 알아봄)
    # 행렬에서 대각선을 이루려면 값이 같아야 하는데..? 어떻게 표현할거냐?
    # 대각선의 값은 2개가 나옴 (0,0)...(n-1,n-1)까지 행,열의 값이 같을때 하나 => 왼쪽 아래에서 오른쪽 위로 상향 => left_low_r
    # (n-1,0)....(0,n-1) 까지 행,열의 값의 합이 n-1을 나타낼 때 하나 =>왼쪽 위에서 오른쪽 아래로 하향 => left_high_r
    dia_low = 0  # 왼쪽 아래서 위로 상향하는 대각선의 초기 값 설정
    dia_high = 0  # 왼쪽 위에서 아래로 하향하는 대각선의 초기 값 설정
    for r in range(100) :
        for c in range(100) :
            if r==c : # => 왼쪽 아래서 오른쪽 위로 상향하기 위한 조건을 충족하냐?
                # dia_low = a[r][c] # => dia_low 의 현재 위칫갑
                dia_low += baeyeul[r][c] # 대각선을 이루는 모든 값들의 총합
                if dia_low > max_val : #dia_low의 값이 max_val보다 큰가 확인
                    max_val = dia_low #dia_low의 값이 max_val보다 크면 max_ val의 값을 변경
            if r+c == 99 : # 왼쪽 위에서 오른쪽 아래로 하향하기 위한 조건을 충족하는가?
                # dia_high = baeyeul[r][c] #dia_high 의 현재 위치값
                dia_high += baeyeul[r][c] # 좌상 우 하로 이동하는 대각선의 값들의 총합
                if dia_high > max_val : # dia_high 의 값이 max_val의 값보다 큰지 확인
                    max_val = dia_high #dia_high 의 값이 크다면 max_val의 값을 변경

    print(f"#{tc} {max_val}")