import sys
sys.stdin = open('input.txt')

# tc의 개수를 10개로 정해줌
for tc in range(10):
    N = int(input())
    arr = list(map(int, input().split()))

    #조망권을 확보받은 세대수를 더해나갈 값 설정
    ans = 0
    # 모든 빌딩에 대해 조망권이 확보된 세대수를 계산
    # i => 2 ~ N - 3
    #앞 뒤 2칸은 빌딩이 없으므로 range범위에서 빼줌
    for i in range(2, N - 2):
        # i번 빌딩의 조망권 계산
        # [i - 2], [i - 1], [i + 1], [i + 2]
        # max_val = max(arr[i-2], arr[i-1], arr[i+1], arr[i+2])
        #i의 앞 뒤 2번째 값을 하나씩 비교하여 그 중 가장 높은 층을 찾음
        max_val = arr[i - 2]
        if max_val < arr[i - 1]:
            max_val = arr[i - 1]
        if max_val < arr[i + 1]:
            max_val = arr[i + 1]
        if max_val < arr[i + 2]:
            max_val = arr[i + 2]

        # 좌 우 두번째 인덱스 값보다도 나 자신이 가장 크다면 조망권을 확보할 수 있는 세대가 있다는 뜻
        # 좌 우 두번째 빌딩까지 중 가장 높았던 빌딩과 자신의 빌딩 차를 구함
        if arr[i] > max_val:
            ans += arr[i] - max_val

    print(f'#{tc + 1} {ans}')