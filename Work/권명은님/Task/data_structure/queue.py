'''
큐(Queue)

선입선출(FIFO - First in, First Out)구조를 가지는 큐 자료구조를 구현해보자!

1. 스택 클래스 선언
   클래스명 : Queue
2. 자료 삽입 메소드
   메소드명 : enqueue
3. 자료 출력 메소드
   메소드명 : dequeue
   ※단, 입력된 자료가 존재하지 않으면 "Queue is Empty" 라는 문구를 출력할 것
'''
#1. 큐 클래스 선언
class Queue():
    def __init__(self):
        self.queue = []

    #2. 자료 삽입 메소드
    def enqueue(self, data):
        self.queue.append(data)
    
    #3. 자료 출력 메소드
    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            print(self.queue.pop(0))

    def isEmpty(self):
        return True if len(self.queue) == 0 else False

queue = Queue()

queue.dequeue() #Queue 출력, 입력값이 없으므로 "Queue is Empty"출력
queue.enqueue(1) # 1 입력
queue.enqueue("test") # "test" 입력
queue.enqueue(3) # 3 입력
queue.dequeue() # 1 출력 (가장 처음에 입력한 값)
queue.dequeue() # "test" 출력
queue.dequeue() # 3 출력
queue.dequeue() #모든 입력값을 출력해 현재 존재하는 값이 없으므로 "Queue is Empty"출력
