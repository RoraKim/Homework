T = int(input())

LEFT = 0  # 왼쪽
RIGHT = 1  # 오른쪽


def bin_search(arr, target, start, end, d):
    if start > end:  # 종료조건
        return 0
    mid = (start + end) // 2  # 중간 찾기
    if arr[mid] == target:  # 만약 탐색 하다가 target 찾으면 1 리턴
        return 1
    elif arr[mid] > target:  # target이 왼쪽 리스트에 있을 때
        if d == LEFT:  # 이전에도 왼쪽 리스트를 찾았었다면 0 리턴
            return 0
        return bin_search(arr, target, start, mid - 1, LEFT)  # 아니라면 다음 왼쪽 리스트에서 탐색 진행
    else:
        if d == RIGHT:  # target에 오른쪽 리스트에 있을 때
            return 0  # 이전에도 오른쪽 리스트를 찾았었다면 0 리턴
        return bin_search(arr, target, mid + 1, end, RIGHT)  # 아니라면 다음 오른쪽 리스트에서 탐색 진행


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = 0

    a.sort()

    for num in b:  # b 원소들 a에서 이진탐색으로 찾기
        result += bin_search(a, num, 0, N - 1, -1)

    print(f'#{tc} {result}')