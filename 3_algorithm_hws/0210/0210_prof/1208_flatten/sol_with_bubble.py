import sys
sys.stdin = open('input.txt')

def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

for tc in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))

    # N번 덤프
    for i in range(dump):
        bubble_sort(boxes)
        # 정렬 (배웠던 버블 정렬 활용)
        # 처음과 끝을 계속 정렬하면서 평탄화
        boxes[0] += 1
        boxes[-1] -= 1

    # 덤프 이후 최종 정렬
    bubble_sort(boxes)
    result = boxes[-1] - boxes[0]
    print(f'#{tc} {result}')