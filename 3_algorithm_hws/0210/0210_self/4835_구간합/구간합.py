
import sys
sys.stdin = open('구간합.txt')

# tc 갯수
T = int(input())

for tc in range(1, T + 1):
    n, m = map(int,input().split())
    num = list(map(int, input().split()))

    min_sum = 100000000000000000000000
    max_sum = 0
    for i in range(n - m + 1):
        result = 0
        for j in range(i, i + m):
            result += num[j]

        if result > max_sum:
            max_sum = result
        if result < min_sum:
            min_sum = result

    print(f'#{tc}', max_sum - min_sum)























import sys
sys.stdin = open('구간합.txt')

# tc 갯수
T = int(input())

for tc in range(1, T + 1):

    # n - 정수 수
    # m - 이웃한 m개
    n, m = map(int, input().split())
    num = list(map(int, input().split()))

    #최소는 충분히 큰 값, 최대는 작은값
    min_sum = 100000000000000000
    max_sum = 0

    #이웃한 개수 n개 : i + n-1까지
    #전체 10개 중 인접한 3개까지 찾으려면 8까지 순회해야함(인덱스 7) 8 9 10 이후로는 벗어남 = 10 -3 + 1
    for i in range(n - m + 1):
        # 합 저장해 줄 변수 result
        result = 0
        # 이웃한 n개의 합을 더해서 반환하는 result
        for j in range(i, i + m):
            result += num[j]

        # result가 min보다 작다면 min에 넣고, max보다 크다면 max에 넣음
        if result < min_sum:
            min_sum = result
        if result > max_sum:
            max_sum = result

    minus = max_sum - min_sum
    print(f'#{tc} {max_sum - min_sum}')




