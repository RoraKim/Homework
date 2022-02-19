import sys
sys.stdin = open('input.txt', encoding='utf-8')

def bruteForce(pattern, target):
    # 현재 조사중인 target의 인덱스
    t_idx = 0
    # 현재 조사중인 pattern의 인덱스
    p_idx = 0
    # 찾은 개수
    count = 0
    # pattern 조사 idx가 pattern 길이보다 작고
    # target 조사 idx가 word 길이보다 작은동안
    while p_idx < len(pattern) and t_idx < len(target):
        # target 중 현재 조사 대상
        a = target[t_idx]
        # char 중 현재 조사 대상
        b = pattern[p_idx]

        # 조사 대상이 일치하지 않다면
        if a != b:
            # 다음 word 조사 idx 초기화
            # 패턴 길이만큼 과거로 돌아가서 다시 조사
            t_idx = t_idx - p_idx
            # 다음 pattern 조사 idx 초기화
            p_idx = -1

        # 다음칸으로 이동
        t_idx += 1
        p_idx += 1

        # 만약 모든 단어를 조사했다면
        if p_idx == len(pattern):
            # 패턴 일치
            count += 1
            # 다음 대조 대상 초기화
            p_idx = 0
    return count


for _ in range(10):
    tc = int(input())
    pattern = input()
    target = input()

    print(f'#{tc} {bruteForce(pattern, target)}')

