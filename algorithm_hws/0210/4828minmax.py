import sys
sys.stdin = open("4828.txt")

T = int(input())

# 출력 : #tc max-min 의 형태
# tc값을 출력해야 하기 때문에 range 1부터 시작해야 첫번째 tc값이 1이 된다
for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))


    # 한바퀴를 돌고나면 맨 마지막에 가장 큰 값이 위치하게 버블정렬 이용
    # 그 다음 바퀴는 맨 마지막값을 제외하고 비교함
    # 역순으로 i를 꺼낸다
    for i in range(N-1, 0, -1):

        #앞쪽 인덱스값이 뒤쪽 인덱스 값보다 더 크면 더 뒤로 이동해야하기 때문에 위치를 바꿔줌
        for j in range(0, i):
            if a[j] > a[j + 1]:
                a[j], a[j+1] = a[j+1], a[j]

    #result는 가장 큰 값이 맨 마지막에 위치, 가장 작은 값이 맨 처음에 위치되어 있는 상태
    result = a[-1] - a[0]
    #출력 형태에 맞게 변경
    print(f'#{tc} {result}')
