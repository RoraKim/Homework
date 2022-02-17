import sys
sys.stdin = open('4864_문자열비교.txt')

def len(array):
    count = 0
    for i in array:
        count += 1

    return count


t = int(input())
for tc in range(1, t+1):
    sub = input()
    main = input()
    n = len(sub)
    m = len(main)

    #브루트 포스에 사용할 main과 sub의 인덱스 값을 설정한다.
    #main의 첫번째, sub의 첫번째 인덱스부터 검사하므로 둘다 0으로 설정
    #비교해서 같으면 둘 다 다음 인덱스를 조사해야 하기때문에 +1을 해줌
    #비교해서 다르면  main인덱스의 다음 인덱스부터 조사해야하기 때문에 i에만 1을 더해줌
    i = 0
    j = 0
    while i < m and j < n:
        if main[i] == sub[j]:
            i += 1
            j += 1

        elif main[i] != sub[j]:
            i += 1
            j = 0

    #while문이 끝났다는 것은 i가 main의 끝에 도달했거나, j가 sub의 끝에 도달했거나 둘 다 라는 뜻
    #j가 sub 끝 인덱스까지 갔다는 것은 마지막 비교에서도 j가 1 증가했다는 것을 의미함
    #즉 마지막 글자까지 일치했다는 뜻
    if j == n:
        # print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')







