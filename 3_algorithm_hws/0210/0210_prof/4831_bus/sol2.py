import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    data = list(map(int, input().split()))


    # 정류소 도표화
    station = [0]*(N+1)
    # 충전소 위치 표시
    for i in data:
        station[i] = 1

    # 현재 위치
    now = 0
    # 충전 횟수 : 처음 시작할때 충전은 횟수로 치지 않음
    count = -1
    # 이동할 수 있는 거리
    mov = K
    while True:
        # 현재위치 + 이동할 수 있는 거리에 정류소가 있다면
        if station[now+mov]:
            # 이동
            now += mov
            # 충전 횟수 += 1
            count += 1
            # 이동 가능 거리 초기화
            mov = K
        # now + mov에 정류소가 없다면
        else:
            # 그 한칸 전 위치 조사
            mov -= 1

        # 계속 조사를 해봤지만 정류소가 없어서
        # 이동 할 수 있는 거리가 0이 되면
        if mov == 0:
            # 도착 불가
            count = 0
            break

        # 현재위치 + 이동가능거리가 최대 정류소를 넘어선다면
        if now + mov >= N:
            # 현재 위치에서 충전하고 도착
            count += 1
            break

    print(f'#{tc} {count}')