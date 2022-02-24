import sys; sys.stdin = open('4874_forth.txt')

def len(arr):
    cnt = 0
    for i in arr:
        cnt += 1
    return cnt

t = int(input())
for tc in range(1, t + 1):
    arr = list(input().split())
    # print(arr)
    stack = [] * len(arr)

    for i in arr:
        # 연산자에 해당하면
        if i in ('+', '-', '/', '*'):
            try:
                b = stack.pop()
                a = stack.pop()
                if i == '+':
                    c = int(a) + int(b)
                if i == '-':
                    c = int(a) - int(b)
                if i == '/':
                    c = int(a) // int(b)
                if i == '*':
                    c = int(a) * int(b)
                stack.append(c)
            # 연산자가 나왔는데도 연달아 pop할 원소가 없다는 것은
            # 에러라는 뜻
            except:
                print(f'#{tc} error')
                # 한번 에러가 발생하면 다음걸 볼 필요 없음
                break

        # 마지막까지 도착해서 .을 만났다면
        elif i == '.':
            # stack에 하나만 남아있어야함
            if len(stack) == 1:
                print(f'#{tc}', *stack)
            else:
                print(f'#{tc} error')
                break

        # 숫자라면 stack에 push
        else:
            stack.append(int(i))

    # print(stack)


# for i in range(3):
#     for i in range(3):
#         if:
#             break
#         if:


# for i in range(3):
#     if:
#         continue
#     if:


