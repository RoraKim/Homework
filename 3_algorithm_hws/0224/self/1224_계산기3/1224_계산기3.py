import sys; sys.stdin = open('1224_계산기3.txt')
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

def post_cal(arr):
    stack = [] * len(arr)

    for i in arr:
        # 연산자에 해당하면
        if i in ('+', '-', '/', '*'):
                b = stack.pop()
                a = stack.pop()
                if i == '+':
                    c = int(a) + int(b)
                elif i == '-':
                    c = int(a) - int(b)
                elif i == '/':
                    c = int(a) // int(b)
                elif i == '*':
                    c = int(a) * int(b)
                stack.append(c)

        else:
            stack.append(int(i))
    return sum(stack)

for tc in range(1,11):
    n = int(input())
    lst = list(input())
    # print(lst)
    stack = Stack(n)

    isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0, ')': 0} #in-stack priority
    icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3} #in-coming priority

    post = []
    for i in lst:
        if i in icp:
            #연산자는 스택이 비었으면 push한다
            if stack.arr[0] == None:
                stack.push(i)

            else:
                #i가 연산자인데 스택이 비어있지 않으면서
                #스택 맨위 연산자의 우선순위가 i보다 같거나 크다면
                #stack의 연산자를 pop한뒤 출력하고
                #현재 i는 스택에 push
                while isp.get(stack.arr[stack.top]) >= icp.get(i):
                    post.append(stack.pop())
                    if stack.is_empty():
                        break
                stack.push(i)
        #숫자이면
        else:
            post.append(i)

    while not stack.is_empty():
        post += stack.pop()
    print(*post)

    # print(f'#{tc}',post_cal(post))