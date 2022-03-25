import sys;sys.stdin = open('5186_이진수2.txt')
#10진수 실수 -> 이진수
#소수점 아래 13자리 까지 이상이면 오버플로우

n = int(input())
for tc in range(1, n+1):
    dec = float(input())

    front = int(dec)

    if front > 0:
        result = bin(front).replace('0b','')
        result = result + '.'
        # print(result)

    else:
        result = '0.'



    back = dec - front

    back_result = ''
    while len(back_result) <13:
        back_result = back_result + str(int(back * 2))
        back = back * 2 - int(back * 2)
        if back == 0:
            break
    # print(back_result)

    if len(back_result) == 13:
        print(f'#{tc} overflow')

    else:
        print(f'#{tc} {back_result}')



