'''
큐(Queue)

선입선출(FIFO - First in, First Out)구조를 가지는 큐 자료구조를 구현해보자!
https://github.com/ktechedu-IoT/StudyGroup/blob/main/Work/%EA%B6%8C%EC%98%A4%EC%A4%80%EB%8B%98/Task/data_structure/queue.py
1. 스택 클래스 선언
   클래스명 : Queue
2. 자료 삽입 메소드
   메소드명 : enqueue
3. 자료 출력 메소드
   메소드명 : dequeue
   ※단, 입력된 자료가 존재하지 않으면 "Queue is Empty" 라는 문구를 출력할 것
'''

class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self,data):
        self.queue.append(data)

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
        else :
            print(self.queue.pop(0))

    def isEmpty(self):
        return True if len(self.queue) == 0 else False

queue = Queue()

queue.dequeue()
queue.enqueue(1)
queue.enqueue("test")
queue.enqueue(3)
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()


# 함수 / class (self) 이해하기
# pop() = pop(-1) / 변수 값 지정 x -> 마지막 요소 제거
# isEmpty 함수 순서(?) / True,False 사용되는 이유

