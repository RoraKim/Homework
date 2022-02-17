import sys
sys.stdin = open('input.txt')

t = int(input())

for i in range(t):
    tc, n = input().split()
    arr = list(map(str, input().split()))
    nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    result = []
    for i in nums:
        for j in arr:
            if j == i:
                result.append(j)

    print(f'{tc}')
    print(*result)














    # result = []
    # for number in nums:
    #     for i in arr:
    #         if i == number:
    #             #앞에서부터 비교하며 같은 값이 나오면 result에 더해줌
    #
    #             result.append(i)
    #             arr.remove(i)
    #
    # print(f'{tc}',' '.join(map(str,result)))
