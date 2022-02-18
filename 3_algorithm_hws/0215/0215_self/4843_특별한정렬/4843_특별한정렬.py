import sys
sys.stdin = open('4843_특별한정렬.txt')
t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    # print(arr)

    #버블 소트
    # n-1 번째 1까지 역순으로 내려간다. 맨 앞과 맨 뒤의 값을 제외해서 2개씩 묶일 수 있도록
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
                # 이전 요소가 이후 요소보다 크면 교환
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    #큰 값이 앞으로 온 정렬
    reverse = arr[::-1]
    #큰 값이 뒤로 온 정렬
    origin = arr

    new_arr = []
    for i in range(5):
        new_arr.append(reverse[i])
        new_arr.append(origin[i])

    #print(f'#{tc}',*new_arr)
    print(f'#{tc}',' '.join(map(str, new_arr)))