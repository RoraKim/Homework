import sys; sys.stdin = open('단순2진암호코드.txt')


code = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4, '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9}
t = int(input())


for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int,input()))for _ in range(n)]

    # idx_lst = []
    last_i = 0
    for i in range(n -1, -1, -1):
        for j in range(m -1, -1, -1):
            if arr[i][j] == 1:
                last_i = i
                last_j = j
                # idx_lst.append([last_i,last_j])

                # print(last_i, last_j)
                break
        if last_i > 0:
            break

    # print(last_i, last_j)
    # print(idx_lst)


    decode = []
    for k in range(last_j-55, last_j +1, 7):
        # print(k)
        # print(arr[last_i][k:k+7])
        key = ''.join(map(str, arr[last_i][k:k+7]))
        # print(key)
        decode.append(code.get(key))
        # print(arr[last_i][k])
    # print(decode)

    cal_decode = (decode[0] + decode[2] + decode[4] + decode[6]) * 3 + decode[1] + decode[3] + decode[5] + decode[7]
    # print(cal_decode)
    if cal_decode % 10 == 0:
        print(f'#{tc} {sum(decode)}')

    else:
        print(f'#{tc} 0')

    # print("=" * 30)


