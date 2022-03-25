import sys;sys.stdin = open('5185_이진수.txt')
#16진수 -> 2진수

def binary(num):
    binn = ''

    while num > 1:
        binn = str(num % 2) + binn
        num = num // 2
    binn = str(num) + binn

    while len(binn) < 4:
        binn = '0' + binn

    return binn


alpha = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

def convert_alpha(hex):
    result = ''
    for i in range(n):
        if hex[i] in alpha:
            # print(hex[i])
            convert = alpha.get(hex[i])
            result += binary(convert)
            # print(convert)

        else:
            intt = int(hex[i])
            result += binary(intt)

    return result



t = int(input())
for tc in range(1, t + 1):
    n, hex = input().split()
    n = int(n)

    print(f'#{tc} {convert_alpha(hex)}')

