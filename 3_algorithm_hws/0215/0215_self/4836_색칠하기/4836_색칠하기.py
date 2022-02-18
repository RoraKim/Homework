import sys
sys.stdin = open('4836_색칠하기.txt')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    #10 * 10행렬을 만들어서
    #그 안의 숫자를 더해가자
    #빨간색, 파란색 박스가 차지하는 영역의 숫자가 다 더해진 후 값이 3이면 보라색 영역이다.
    my_list = [[0 for _ in range(10)]for _ in range(10)]
    count = 0
    for _ in range(n):
        x1, y1, x2, y2, c = map(int, input().split())
        #x1에서 x2까지 가로 영역에 해당 색 값을 넣어줌
        for x in range(x1, x2+1):
            #y1에서 y2까지 세로 영역에 해당 색 값을 넣어줌
            for y in range(y1, y2+1):
                my_list[x][y] += c

    #전체 행렬에서 값이 3인 갯수를 찾음
    for i in range(10):
        for j in range(10):
            if my_list[i][j] == 3:
                count += 1

    print(f'#{tc} {count}')








