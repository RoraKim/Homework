import sys
sys.stdin = open('input.txt')

t = int(input())

for i in range(t):
    tc, n = input().split()
    words = input().split()
    numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    result = []
    for number in numbers:
        for word in words:
            if word == number:
                #앞에서부터 비교하며 같은 값이 나오면 result에 더해줌
                result.append(number)

    print(f'{tc}',' '.join(map(str,result)))
