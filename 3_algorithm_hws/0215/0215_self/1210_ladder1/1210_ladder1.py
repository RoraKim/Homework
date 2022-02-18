
import sys; sys.stdin = open('1210_ladder1.txt')

# 도착점과 연결되어있는 출발점을 찾자
for tc in range(1, 11):
    N = int(input())
    #앞 뒤로 0을 추가해 범위를 벗어나지 않게 해줌
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]  # 일단 값을 받아오자

    #뒤에서부터 찾기
    #맨뒤의 값이 2인 지점의 인덱스를 찾아라
    finish_line_idx = arr[99].index(2)
    # print(finish_line_idx)

    #맨 마지막 줄에서 왼, 오를 탐색하고 왼, 오가 없으면 위로 가자
    # arr의 첫 줄에 도착할 때 까지

    last = 99
    finish_line = arr[last][finish_line_idx]

    #왼 오 위
    di = [0, 0, -1]
    dj = [-1, 1, 0]

    while last > 0:

    #지나온 길을 0으로 바꾸기
    #왼 위 있으면 왼
        if arr[last][finish_line_idx - 1] == 1 and arr[last -1][finish_line_idx] ==1:
            finish_line_idx += dj[0]
            arr[last][finish_line_idx] = 0
        #오 위 있으면 오
        if arr[last][finish_line_idx + 1] == 1 and arr[last -1][finish_line_idx] ==1:
            finish_line_idx += dj[1]
            arr[last][finish_line_idx] = 0

        #왼 있으면 왼
        if arr[last][finish_line_idx - 1] == 1:
            finish_line_idx += dj[0]
            arr[last][finish_line_idx] = 0

        #오 있으면 오
        if arr[last][finish_line_idx + 1] == 1:
            finish_line_idx += dj[1]
            arr[last][finish_line_idx] = 0

        #위 있으면 위
        if arr[last - 1][finish_line_idx] == 1:
            last += di[2]
            arr[last][finish_line_idx] = 0

    print(f'#{tc} {finish_line_idx - 1}')

    # # finish_line에서 주변을 조회해보자. 위, 왼 모두 1이면 왼쪽으로 -> finish_line_idx에 dj[0] 더해주자
    # # 위, 오 모두 1이면 오른쪽으로 -> finish_line_idx에 dj[2] 더해주자
    # # 위만 1이면 위쪽으로 -> end값에 di[1] 더해주자
    # # 지나온 길의 값은 0으로 바꿔주어야 되돌아가지 않음
    #
    # while end > 0:  # 첫 줄에 도달할 때 까지
    #     # 근데 아래의 경우는 finish_line_idx가 오른쪽 끝이거나 왼쪽 끝일 경우 조건을 확인하는 과정에서 인덱스 에러가 뜰 것임
    #     # 그래서 처음 배열 받아올 때 양 끝에 [0] 추가해줌
    #     if arr[end - 1][finish_line_idx] == 1 and arr[end][finish_line_idx - 1] == 1:  # 위, 왼이 모두 1일때
    #         finish_line_idx += dj[0]
    #         arr[end][finish_line_idx] = 0
    #     elif arr[end - 1][finish_line_idx] == 1 and arr[end][finish_line_idx + 1] == 1:  # 위, 오가 모두 1일때
    #         finish_line_idx += dj[2]
    #         arr[end][finish_line_idx] = 0
    #     elif arr[end - 1][finish_line_idx] == 1:  # 위가 1일때
    #         end += di[1]
    #         arr[end][finish_line_idx] = 0
    #     elif arr[end][finish_line_idx - 1] == 1:  # 왼이 1일때
    #         finish_line_idx += dj[0]
    #         arr[end][finish_line_idx] = 0
    #     elif arr[end][finish_line_idx + 1] == 1:  # 오가 1일때
    #         finish_line_idx += dj[2]
    #         arr[end][finish_line_idx] = 0
    #
    # print(f'#{tc} {finish_line_idx - 1}')  # 앞에 [0] 하나를 추가해줬기 때문