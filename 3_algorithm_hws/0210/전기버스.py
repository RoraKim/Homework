import sys
sys.stdin = open('전기버스.txt')

#tc 갯수
t = int(input())
for tc in range(1, t+1):

    #k : 한번 충전으로 최대한 이동할 수 있는 정류장 수
    #n : 종점 정류장
    #m : 충전기가 설치된 정류장 수
    k, n, m = map(int, input().split())

    #충전기가 설치된 정류장 번호
    stop_num = list(map(int, input().split()))
    # print(n)
    # print(stop_num)

    for i in range(0,n+1):
