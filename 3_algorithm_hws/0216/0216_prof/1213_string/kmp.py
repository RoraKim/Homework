import sys
sys.stdin = open('input.txt', encoding='utf-8')

def KMP(pattern, target):
    p_idx = 0
    p_len = len(pattern)
    t_idx = 0
    t_len = len(target)
    cnt = 0
    while p_idx < p_len and t_idx < t_len:
        a = pattern[p_idx]
        b = target[t_idx]
        # 매칭되지 않을 때,
        if a != b:
            # 패턴의 첫글자였다면
            if p_idx == 0:
                # target의 조사대상만 1 이동
                t_idx += 1
            # 아니면
            else:
                # target은 그대로, p만 처음부터
                p_idx = 0
        # 두 글자가 같다면
        else:
            # 다음 조사 위치로
            t_idx += 1
            p_idx += 1

        if p_idx == p_len:
            cnt += 1
            p_idx = 0
    return cnt

for _ in range(10):
    tc = int(input())
    pattern = input()
    target = input()

    print(f'#{tc} {KMP(pattern, target)}')