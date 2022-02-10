import sys
sys.stdin = open('input.txt')
# 빌딩들의 높이가 정수 리스트로 저장
for tc in range(10):
    N = int(input())
    arr = list(map(int, input().split()))

    ans = 0
    # 모든 빌딩에 대해 조망권이 확보된 세대수를 계산
    # i => 2 ~ N - 3
    for i in range(2, N - 2):
        # i번 빌딩의 조망권 계산
        # [i - 2], [i - 1], [i + 1], [i + 2]
        # max_val = max(arr[i-2], arr[i-1], arr[i+1], arr[i+2])
        max_val = arr[i - 2]
        if max_val < arr[i - 1]:
            max_val = arr[i - 1]
        if max_val < arr[i + 1]:
            max_val = arr[i + 1]
        if max_val < arr[i + 2]:
            max_val = arr[i + 2]

        if arr[i] > max_val:
            ans += arr[i] - max_val

    print(f'#{tc + 1} {ans}')




