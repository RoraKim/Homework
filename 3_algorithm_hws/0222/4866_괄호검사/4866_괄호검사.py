import sys; sys.stdin = open('4866_괄호검사.txt')

class Stack:
    def __init__(self, size):
        self.size = size
        self.arr = [None] * size
        self.top = -1

    def push(self, n):
        self.top += 1
        self.arr[self.top] = n

    def pop(self):
        if not self.is_empty():
            result = self.arr[self.top]
            self.arr[self.top] = None
            self.top -= 1
            return result

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False


def remove_match(n):
    s1 = Stack(n)
    for i in range(n):
        #필요한 문자는 stack에 넣는다
        if words[i] in ('{','}','(',')'):
            s1.push(words[i])

        # 현재 top 직전의 문자와 현재의 문자가 짝을 이루는 괄호라면
        if s1.arr[s1.top - 1] == '(':
            if words[i] == ')':
                #현재 문자도 pop
                s1.pop()
                #짝을 이루는 앞 문자도 pop
                s1.pop()

        if s1.arr[s1.top - 1] == '{':
            if words[i] == '}':
                s1.pop()
                s1.pop()

    return s1.arr

t = int(input())
for tc in range(1, t + 1):
    words = input()
    lenn = len(words)
    s1 = Stack(lenn)

    for i in range(lenn):
        result = remove_match(lenn)
    # print(result)

    cnt = 0
    for i in range(lenn):
        if result[i] is not None:
            cnt += 1

            if cnt > 0:
                print(f'#{tc}', 0)
                break
    else:
        print(f'#{tc}', 1)




