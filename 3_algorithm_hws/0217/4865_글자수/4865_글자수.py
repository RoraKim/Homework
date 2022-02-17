import sys; sys.stdin = open('4865_글자수.txt')


def len(array):
    count = 0
    for i in array:
        count += 1

    return count


t = int(input())
for tc in range(1, t + 1):
    sub = input()
    main = input()
    n = len(sub)
    m = len(main)
    # 비교문자열은 sub안에 속해있기 때문에 배열의 크기는 sub의 길이만큼이다.
    arr = [0] * n
    # print(arr)

    # arr에 카운팅한 값을 넣어준다
    # main의 알파벳이 sub에 있다면 arr의 해당 알파벳 인덱스를 찾아 값을 늘려주면 카운트가 누적이된다.
    for i in range(m):
        for j in range(n):
            if main[i] == sub[j]:
                arr[j] += 1

    #arr 안에서 가장 큰 값을 찾아낸다.
    # print(arr)
    max_num = 0
    for i in arr:
        if i > max_num:
            max_num = i

    print(f'#{tc}', max_num)


