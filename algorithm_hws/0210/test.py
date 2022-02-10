import sys
sys.stdin = open('4834.txt')
#테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    numbers = int(input())
    counter = [0 for _ in range(10)]
    a = list(map(int, input()))

    # print(a)
    for number in a:
        counter[number] += 1

for i in range(1, len(counter)):
    counter[i] += counter[i - 1]
print(counter)

# 3. result 생성
result = [-1] * len(a)
print(result)

# 4. result_arr에 정렬하기(counting_arr를 참조)
for i in range(len(result) - 1, -1, -1):
    counter[a[i]] -= 1
    result[counter[a[i]]] = a[i]

print(result)
# for i in input_arr:
#     counting_arr[i] -= 1
#     result_arr[counting_arr[i]] = i
#
# return result_arr
