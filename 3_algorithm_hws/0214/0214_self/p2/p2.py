import sys; sys.stdin = open('p2.txt')

T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = len(arr)
    for i in range(1, 1<<N):
        result = 0
        for j in range(N):
            if i & 1<<j:
                result += arr[j]

        if result == 0:
            print(1)
            break

    else:
        print(0)
        # print(result)