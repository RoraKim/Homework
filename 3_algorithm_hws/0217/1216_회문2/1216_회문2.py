import sys; sys.stdin = open('1216_회문2.txt')

#len함수 디파인
def len(arr):
    count = 0
    for i in arr:
        count += 1
    return count

#회문 함수 디파인
#회문이면 word에 담기도록 함
def pelin(word, m):
    m = len(word)
    words = ''
    for i in range(m):
        if word[i] == word[-1 - i]:
            words += word[i]

    return words


for tc in range(1, 2):
    t = int(input())
    arr = [input()for _ in range(100)]
    n= 100
    # print(arr)

    #세로로 펠린드롬을 어떻게 찾아야 할 지 몰라
    #그냥 세로배열을 가로로 바꾼 새 배열을 만들었다..
    new_arr = []  # 세로 배열
    result = ''
    for i in range(100):
        for j in range(100):
            result += arr[j][i]
        new_arr.append(result)

    # print(new_arr)

    max_len = ''
    for i in range(n):
        for j in range(n):
            for m in range(10, 0, -1):
                if len(pelin(arr[i][j:j + m:], m)) > len(max_len):
                    max_len = pelin(arr[i][j:j + m:], m)
                # print(f'#{tc}', pelin(arr[i][j:j + m:], m))

    for i in range(n):
        for j in range(n):
            for m in range(10, 0, -1):
                if len(pelin(new_arr[i][j:j + m:], m)) > len(max_len):
                    max_len = pelin(new_arr[i][j:j + m:], m)

    print(f'{tc}',max_len)