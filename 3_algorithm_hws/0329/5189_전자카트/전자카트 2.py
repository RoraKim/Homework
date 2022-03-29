from itertools import permutations
import sys; sys.stdin = open('5180_전자카트.txt')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    cases = list(permutations([i for i in range(1, N)]))
    results = 99999999999
    for case in cases:
        sub_results = 0
        x = 0
        for c in case:
            sub_results += matrix[x][c]
            print(sub_results)
            x = c
        sub_results += matrix[x][0]
        if sub_results <= results:
            results = sub_results

    # print("#{} {}".format(test_case, results))