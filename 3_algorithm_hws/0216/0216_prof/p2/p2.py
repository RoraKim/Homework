import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    word = int(input())
    result = ''

    is_negative = False

    if word < 0:
        word = word * -1
        is_negative = True

    while word > 0:
        # 1234 => 1의 자리, 10의 자리, 100, ....
        # 10으로 나눴을때의 나머지 값들 활용
        # 0 -> 48
        # 4 -> 4 + 48
        result = chr(word % 10 + 48) + result
        # 1234 // 10 -> 123
        # word = 123
        word = word // 10

    if is_negative:
        result = '-' + result

    print(f'#{tc} {result} {type(result)}')
