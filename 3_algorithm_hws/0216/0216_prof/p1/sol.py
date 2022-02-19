import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    word = input()

    result = ''
    for i in range(len(word)-1, -1, -1):
        result += word[i]
    print(f'#{tc} {result}')
