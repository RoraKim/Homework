# strcmp
def str_comparison(str1, str2):
    # 비교에 활용하는 인덱스
    i = 0

    # 만약 1과 2의 길이 자체가 다르다면 매칭 될 수 없다.
    if len(str1) != len(str2):
        # 끝
        return False
    # 길이가 같은 경우
    # 두 개의 단어보다 i 인덱스의 크기가 작은 상태에서 비교를 진행하다가
    while i < len(str1) and i < len(str2):
        # i번째 인덱스의 요소가 다르면
        if str1[i] != str2[i]:
            # 바로 False
            return False
        # 다르지 않다면 다음 인덱스 요소 확인
        i += 1
    # 최종적으로 다 확인되면 모두 같다는 의미 -> True
    return True


str1 = "abccd"
str2 = "abcd"

# 1. 방법 1
# strcmp
print(str_comparison(str1, str2))

# 2. 방법 2
print(str1 == str2)