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
      self.Queue =[]

#2. 자료 삽입 메소드
   def push(self, data):
      self.Queue.append(data)

#3.  자료 출력 메소드      
   def pop(self, value=0):
      if self.isEmpty():
         print("Queue is Empty")
      else:
         print(self.Queue.pop(value))

   def isEmpty(self):
      return True if len(self.Queue) == 0 else False

#4. 자료 확인용 메소드 
   def show(self):
      return print(self.Queue)

#테스트 코드
#Queue 클래스의 인스턴스 생성
queue = Queue()

queue.pop() #Queue 출력, 입력값이 없으므로 "Queue is Empty"출력
queue.push(1) # 1 입력
queue.push("test") # "test" 입력
queue.push(3) # 3 입력
queue.pop() # 3 출력 (가장 마지막에 입력한 값)
queue.pop() # "test" 출력
queue.pop() # 1 입력
queue.pop() #모든 입력값을 출력해 현재 존재하는 값이 없으므로 "Queue is Empty"출력
queue.show()