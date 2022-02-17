import sys; sys.stdin = open('4861_회문.txt')

#len함수 디파인
def len(arr):
    count = 0
    for i in arr:
        count += 1
    return count

#회문 함수 디파인
#회문이면 word에 담기도록 함
def pelin(word, n):
    words = ''
    for i in range(n):
        if word[i] == word[-1 - i]:
            words += word[i]

    return words

t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    arr = [input()for _ in range(n)]
    # print(arr)

    #세로로 펠린드롬을 어떻게 찾아야 할 지 몰라
    #그냥 세로배열을 가로로 바꾼 새 배열을 만들었다..
    new_arr = []  # 세로 배열
    for i in range(n):
        result= ''
        for j in range(n):
            result += arr[j][i]
        new_arr.append(result)
    # print(new_arr)

    #기존 가로 배열에서의 펠린드롬 찾기
    for i in range(n):
        for j in range(n - m + 1):
            #pelin함수의 결과는 주어진 m길이만큼 다 회문일 경우 길이가 m
            if len(pelin(arr[i][j:j+m:],m)) == m:
                print(f'#{tc}',pelin(arr[i][j:j+m:],m))

    #기존 세로 배열에서의 펠린드롬 찾기
    for i in range(n):
        for j in range(n - m + 1):
            if len(pelin(new_arr[i][j:j + m:], m)) == m:
                print(f'#{tc}', pelin(new_arr[i][j:j + m:], m))







