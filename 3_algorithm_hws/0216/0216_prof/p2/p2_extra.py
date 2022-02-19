import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    word = int(input())
    result = ''
    str_num = '0123456789'

    is_negative = False
    if word < 0:
        word = word * -1
        is_negative = True

    while word > 0:
        result = str_num[word % 10] + result
        word = word // 10

    if is_negative:
        result = '-' + result

    print(f'#{tc} {result} {type(result)}')
