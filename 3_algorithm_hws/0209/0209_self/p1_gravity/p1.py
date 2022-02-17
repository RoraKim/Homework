import sys;

sys.stdin = open('gravity.txt')
tc = int(input())
for tc in range(1, tc + 1):
    n = int(input())
    boxs = list(map(int, input().split()))

    # for 문을 다 돌고 나서나온 max_height들을 저장해서 하나씩 비교
    result = 0
    for i in range(n):
        # 아무것도 안만났을때 최고 낙차
        # 총 9개 칸의 0번째는 최대 낙차가 8
        max_height = len(boxs) - (i + 1)

        # 나보다 큰 것을 하나 만났을 때
        # 중력을 적용받으면 그 위로 떨어지게됨
        # 나의 낙차가 1 줄음
        for j in range(i + 1, n):
            if boxs[i] <= boxs[j]:
                max_height -= 1

            # 전체를 순회하고 나온 max_height 값 중에 가장 큰 값 찾기
        if result < max_height:
            result = max_height

    print(result)

    # result = 0
    # # 모든 상황에 대한 낙찻값 구하기 위한 순회
    # for i in range(N):
    #     # i번째의 최대 낙차 값은
    #     # 전체 길이 - 내 현재 위치 + 1
    #     max_height = len(numbers) - (i+1)
    #
    #     # i번째부터 끝까지 반복해서 더큰값 찾기
    #     for j in range(i+1, len(numbers)):
    #         # i보다 큰 j 찾기
    #         # 찾으면 최대 낙차 -1
    #         if numbers[i] <= numbers[j]:
    #             max_height -= 1
    #
    #     # 최종 최대 낙차 값을 도출
    #     if result < max_height:
    #         result = max_height
    # print(f'#{tc} {result}')
























# import sys; sys.stdin = open('gravity.txt', encoding='UTF-8')
#
#
# def gravity(arr, n):
#     grav_count = 0
#     for i in range(n):
#         for j in range(i + 1, n):
#             if arr[i] > arr[j]:
#                 grav_count += 1
#
#             elif arr[i] <= arr[j]:
#                 grav_count += 1
#                 return grav_count
#     return grav_count
#

# tc = int(input())
# for tc in range(1, tc + 1):
#     n = int(input())
#     boxs = list(map(int, input().split()))
#     print(boxs)
    # max_box = 0
    # for i in range(n):
    #     if max_box < gravity(boxs, n):
    #         max_box = gravity(boxs, n)
    #
    # print(max_box)

    # print(gravity(boxs, n))
    # grav_count = 0
    # for i in range(n):
    #     for j in range(i,n):
    #         if boxs[i] > boxs[j]:
    #             grav_count += 1
    #
    #
    #         elif boxs[i] <= boxs[j]:
    #             continue
                # print(grav_count)


        # print(grav_count)

#
# n = 9
# boxs = [7, 4, 2, 0, 0, 6, 0, 7, 0]
# count_array = [0] * n
# max_box = 0
# # print(count_box)
# for i in range(n):
#     for j in range(i+1,n):
#         if max_box <= boxs[j]:
#             max_box = boxs[j]
#     count_array[i] += count_array[] -


            # count_array[i] += boxs[i]  boxs[j]
