import sys
sys.stdin = open('input.txt')

def binary_search(start, end, target, cnt):
    middle = (start + end) // 2
    if middle == target:
        return cnt
    else:
        if middle < target:
            # 중간지점부터 시작해야 한다는 조건 필수 확인
            return binary_search(middle, end, target, cnt + 1)
        else:
            return binary_search(start, middle, target, cnt + 1)



T = int(input())

for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    # A, B 각자 조사
    a = binary_search(1, P, A, 0)
    b = binary_search(1, P, B, 0)

    print(f'#{tc}', end=' ')
    # a가 더 오래 걸렸다면 b 승리
    if a > b:
        print('B')
    elif a < b:
        print('A')
    else:
        print(0)

