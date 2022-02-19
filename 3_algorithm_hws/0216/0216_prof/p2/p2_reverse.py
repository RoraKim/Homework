import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    word = input()
    result = 0

    is_negative = False

    if word[0] == '-':
        word = word[1:]
        is_negative = True

    idx = 0
    while idx < len(word):
        result += (ord(word[idx]) - 48) * (10 ** (len(word) - idx - 1))
        idx += 1

    if is_negative:
        result = result * -1

    print(f'#{tc} {result} {type(result)}')
