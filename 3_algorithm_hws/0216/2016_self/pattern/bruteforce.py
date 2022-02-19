p = 'is' #찾을 패턴
t = 'That is book' #전체 텍스트
m = len(p) #찾을 패턴의 길이
n = len(t) #전체 텍스트의 길이

def Bruteforce(p, t):
    i = 0
    j = 0
    #j와 i가 각각 패턴과 전체 텍스트의 길이를 벗어나지 않는 동안
    while j < m and i < n:
        # 패턴의 글자와 텍스트의 글자가 다르면
        if p[j] != t[i]:
            #패턴은 0으로 리셋, i는 다음글자로 가도록
            i = i - j
            #if를 빠져나가자 마자 j + 1로 인해 0이 됨
            j = -1
        #패턴과 텍스트가 일치하면 1씩 증가
        i += 1
        j += 1
    #while문이 끝난 이유가 패턴의 끝에 도달했기 때문이라면
    #어느 인덱스에서부터 패턴이 맞았는지 보여줌줌
    f j == m:
        return i - j

    else:
        return -1



print(Bruteforce(p,t))



#     i = 0
#     j = 0
#     while j < m and i < n:
#         if t[i] != p[j]:
#             i = i - j
#             j = -1
#         i = i + 1
#         j = j + 1
#
#     if j == m:
#         return i - m
#     else:
#         return -1
#
# print(Bruteforce(p,t))