import sys; sys.stdin = open('5789_현주의상자바꾸기.txt')
t = int(input())
for tc in range(1, t+1):
    #n: 상자 수 , m: 작업 횟수
    n, m = map(int, input().split())
    result = [0] * n
    #i번째를 인덱스로 쉽게 변환하기 위해 1부터 시작
    for num in range(1, m + 1):
        l, r = map(int, input().split())
        #1번째 상자의 인덱스는 0이기 때문에 일치시키기 위해 1 뺌
        l -= 1
        r

        # print(l,r)
        for i in range(l,r):
            result[i] = num

    print(f'#{tc}', *result)

