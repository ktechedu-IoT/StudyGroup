'''
스택(Stack)

후입선출(LIFO - Last in, First Out)구조를 가지는 스택 자료구조를 구현해보자!

1. 스택 클래스 선언
   클래스명 : Stack
2. 자료 삽입 메소드
   메소드명 : push
3. 자료 출력 메소드
   메소드명 : pop
   ※단, 입력된 자료가 존재하지 않으면 "Stack is Empty" 라는 문구를 출력할 것
'''

#1. 스택 클래스 선언
class Stack():
    def __init__(self):
        self.stack = []

    #2. 자료 삽입 메소드
    def push(self, data):
        self.stack.append(data)
    
    #3. 자료 출력 메소드
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print(self.stack.pop())

    def isEmpty(self):
        return True if len(self.stack) == 0 else False

#테스트 코드
#Stack 클래스의 인스턴스 생성
stack = Stack()

stack.pop() #Stack 출력, 입력값이 없으므로 "Stack is Empty"출력
stack.push(1) # 1 입력
stack.push("test") # "test" 입력
stack.push(3) # 3 입력
stack.pop() # 3 출력 (가장 마지막에 입력한 값)

stack.pop() # "test" 출력
stack.pop() # 1 입력
stack.pop() #모든 입력값을 출력해 현재 존재하는 값이 없으므로 "Stack is Empty"출력
