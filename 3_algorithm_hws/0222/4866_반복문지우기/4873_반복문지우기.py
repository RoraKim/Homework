import sys;
sys.stdin = open('4873_반복문지우기.txt')

def len(arr):
    cnt = 0
    for i in arr:
        cnt += 1
    return cnt

class Stack:
    #stack  생성하며 top 초기값 0으로 지정
    # arr의 크기 지정
    def __init__(self, size):
        self.size = size
        self.arr = [None] * size
        self.top = -1

    #top은 arr에 값이 추가될 때 마다 증가하기 때문에
    #top이 -1이라는건 arr가 비어있다는 뜻
    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    #top은 0부터 시작하기 때문에
    #size보다 1 작다면 최고 위치 top이라는 뜻
    def is_full(self):
        if self.top == self.size - 1:
            return True
        else:
            return False

    # 현재 위치 한칸 위에 해당 값을 넣어줌
    def push(self, n):
        # 어디에?
        self.top += 1
        self.arr[self.top] = n

    #뺄 값이 없다면 에러반환
    #뺄 값이 있다면 pop으로 반환해서 보여줄 값 미리  result에 저장
    #저장 했으니 기존 값을 None으로 변경하고 top다시 줄여줌
    #pop으로 보여줘야 하는 값은 result
    def pop(self):
        if not self.is_empty():
            result = self.arr[self.top]
            self.arr[self.top] = None
            self.top -= 1
            return result
        else:
            raise IndexError('범위를 벗어남')



def no_repeat(n):
    s1 = Stack(n)
    for i in range(n):
        # 현재 top의 글자와 내가 넣으려는 글자가 다르다면
        # 내가 넣으려는 글자를  push
        if s1.arr[s1.top]  != words[i]:
            s1.push(words[i])

        # 현재 top의 글자가 내가 넣으려는 글자와 같다면
        # 현재 있는 글자를 pop
        elif s1.arr[s1.top]  == words[i]:
            s1.pop()
    return s1.arr


t = int(input())
# print(t)
for tc in range(1, t+ 1):
    words = input()
    lenn = len(words)
    result = no_repeat(lenn)

    cnt = 0
    for i in result:
        if i is not None:
            cnt += 1

    print(f'#{tc}', cnt)

