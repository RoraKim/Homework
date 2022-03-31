# T = int(input())
#
# LEFT = 0  # 왼쪽
# RIGHT = 1  # 오른쪽
#
#
# def bin_search(arr, target, start, end, d):
#     if start > end:  # 종료조건
#         return 0
#     mid = (start + end) // 2  # 중간 찾기
#     if arr[mid] == target:  # 만약 탐색 하다가 target 찾으면 1 리턴
#         return 1
#     elif arr[mid] > target:  # target이 왼쪽 리스트에 있을 때
#         if d == LEFT:  # 이전에도 왼쪽 리스트를 찾았었다면 0 리턴
#             return 0
#         return bin_search(arr, target, start, mid - 1, LEFT)  # 아니라면 다음 왼쪽 리스트에서 탐색 진행
#     else:
#         if d == RIGHT:  # target에 오른쪽 리스트에 있을 때
#             return 0  # 이전에도 오른쪽 리스트를 찾았었다면 0 리턴
#         return bin_search(arr, target, mid + 1, end, RIGHT)  # 아니라면 다음 오른쪽 리스트에서 탐색 진행
#
#
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     a = list(map(int, input().split()))
#     b = list(map(int, input().split()))
#     result = 0
#
#     a.sort()
#
#     for num in b:  # b 원소들 a에서 이진탐색으로 찾기
#         result += bin_search(a, num, 0, N - 1, -1)
#
#     print(f'#{tc} {result}')



#==========================================================


def binary_search(n, left, right):
    global cnt, flag

    while left <= right:
        m = (left + right) // 2
        middle_num = a_nums[m]

        #찾고자 하는 값이 바로 나오면 성공
        if n == middle_num:
            flag = 0
            return flag

        #찾고자 하는 값이 왼쪽에 있다면
        elif n < middle_num:
            #좌로 간다
            cnt += 1
            #직전에도 좌 였다면
            if cnt == 2:
                #flag 1 == 실패이기 때문에 값 변환
                flag = 1
                return flag
            else:
                #위의 if에 안걸렸다는건 좌우좌 이거나 좌 등 문제가 없었다는 뜻
                #좌 값으로 변환해줌
                cnt = 1
            #왼쪽 arr를 중심으로 다시 탐색 시작
            right = m - 1

        elif n > middle_num:
            #우로 간다
            cnt -= 1
            #직전에도 우 였다는 뜻
            if cnt == -2:
                #찾고자 하는 값에 해당 안되기 때문에 flag 변환
                flag = 1
                return flag
            else:
                #위의 if에 안걸렸다는 것은 우좌우 등 앞의 로직에 문제가 없었다는 뜻
                #우 값으로 변환해줌
                cnt = -1
            #오른쪽 arr를 중심으로 다시 탐색 시작
            left = m + 1

    # while을 다 돌아도 못찾았다면 못찾을 때
    return flag


test_case = int(input())
for tc in range(1, test_case + 1):
    a, b = map(int, input().split())
    a_nums = list(map(int, input().split()))
    a_nums.sort()                               #이진탐색은 정렬이 된 상태로 해야함

    b_nums = list(map(int, input().split()))
    length_a = len(a_nums)
    ans = 0

    for b_num in b_nums:                        #b에 있는 값 중에서 a에 있는 값 탐색
        cnt, flag = 0, 1
        result = binary_search(b_num, 0, length_a - 1)
        #print(cnt)
        if not flag:
            ans += 1

    print(f'#{tc} {ans}')