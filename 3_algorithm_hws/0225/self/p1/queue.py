class Queue:
    def __init(self,size):
        self.size = size
        self.items = [None] * size
        self.rear = -1
        self.front = -1

    def enQueue(self, el):
        if self.isFull():
            #여러가지 해결방법
            #1.queue의 크기를 늘린다
            #2. 또 다른 예외처리
            print('Queue is Full!!')
        else:
            self.rear += 1
            self.items[self.rear] = el

    def deQueue(self, el):
        if self.isEmpty():
            #여러가지 해결방법
            #1.queue의 크기를 늘린다
            #2. 또 다른 예외처리
            print('Queue is Empty!!')
        else:
            self.front += 1
            self.items[self.rear] = self.front

    def isEmpty(self):
        return self.rear == self.front

    def isFull(self):
        return self.rear == self.size - 1

    def QPeek(self):
        return self.items[self.front]

q = Queue(3)
print('=' * 10, '최초 생성시 비어있는지', '=' * 10)
print(q.isEmpty())

