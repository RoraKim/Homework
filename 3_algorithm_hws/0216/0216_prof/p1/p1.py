import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    word = input()
    print(f'#{tc} {word[::-1]}')

    result = list(reversed(word))
    print(f'#{tc} {"".join(result)}')

    result = ''
    for i in word:
        result = i + result
    print(f'#{tc} {result}')