def kmp(t, p):
    n = len(t)
    m = len(p)
    lps = [0] * (m + 1)

    j = 0 #일치한 개수 == 비교할 패턴 위치
    lps[0] = -1
    for i in range(1, m):
        lps[i] = j #p[i]이전에 일치한 개수수
        if p[i] == p[j]:
           j += 1

        else:
           j = 0
        lps[m] = j
        print(lps)

        #search
        i = 0 #비교할 텍스트 위치
        j = 0 #비교할 패턴 위치
        while i < n and j <= m:
            if j ==-1 or t[i] == p[j]: #첫글자가 불일치했거나, 일치하면면
                i += 1
                j += 1
            else:
                j = lps[j]
            if j == m:
                print(i - m, end=" ") #패턴의 인덱스 출력
                j = lps[j]
        print()
        return
    
