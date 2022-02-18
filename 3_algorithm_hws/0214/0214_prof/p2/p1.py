import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = len(arr)
    bit = [0]*N

    # 모든 경우의 수 중, 공집합 제외
    for i in range(1, 1 << N):
        result = 0
        # j는 arr의 idx 이므로 0부터 조회하여야
        # 모든 요소 포함여부 확인 가능
        for j in range(N):
            if i & (1<<j):
                # print(arr[j], end=' ')
                result += arr[j]
        # print()

        # 공집합 제외 모든 합이 0 인 경우
        if result == 0 :
            print(f'# {tc} {1}')
            break
    else:
        print(f'# {tc} {0}')