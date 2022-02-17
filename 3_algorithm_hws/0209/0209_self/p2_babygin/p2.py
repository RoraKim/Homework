import sys; sys.stdin = open('input.txt', encoding = 'UTF-8')

def counting_sort(arr, n): #n = 10
    counts = [0] * n
    for i in arr:
        counts[int(i)] += 1
    # print(counts)

    triple = 0
    run = 0
    for i in range(10):
        while counts[i] >= 3:
            counts[i] -= 3
            triple += 1
            # print(counts)

    for i in range(2, 10):
        while counts[i - 2] and counts[i - 1] and counts[i] >= 1:
            counts[i - 2] -= 1
            counts[i - 1] -= 1
            counts[i] -= 1
            run += 1
            # print(counts)

    if run == 1 and triple == 1:
        return 1
    elif run == 2 or triple == 2:
        return 1
    else:
        return 0


t = int(input())
for tc in range(1, t + 1):
    num = input()
    # print(num)

    print(f'#{tc}',counting_sort(num,10))





