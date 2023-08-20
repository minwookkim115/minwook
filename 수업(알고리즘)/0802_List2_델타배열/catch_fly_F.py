T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N = 파리 숫자 범위, M = 파리채 범위
    fly_num = [list(map(int, input().split())) for _ in range(N)]  # 파리 범위

    catch_fly_max = 0 # 잡은 파리 최대 값

    # 파리채 때문에 끝까지 못가니까
    # 전체 범위에서 파리채 범위 뺀 만큼만 범위 지정
    for r in range(N - (M - 1)):
        for c in range(N - (M - 1)):

            catch_fly_sum = 0 # 움직이면서 잡은 파리 합

            # ▲ r과 c가 전체 범위에서 파리채 범위를 뺀만큼 돌면서
            # ▼ r과 c에 파리채 범위를 더한 파리채 행nr, 열nc 생성
            for nr in range(r, r + M):
                for nc in range(c, c + M):
                    # r과 c로 돌면서 nr nc 범위를 더함
                    # if r = 0 c = 0
                    # nr = 0(r)부터 2(M) - 1까지 / nc = 0(c)부터 2(M) - 1까지
                    catch_fly_sum += fly_num[nr][nc]

            # 최대값 구하기
            if catch_fly_max < catch_fly_sum:
                catch_fly_max = catch_fly_sum

    print(f"#{tc} {catch_fly_max}")
