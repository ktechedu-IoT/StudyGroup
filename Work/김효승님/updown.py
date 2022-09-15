import random

randomnum = random.randrange(1,101)
i=0
def updown(num):
  global randomnum , i
  if num < randomnum:
    i+=1
    return 'up'
  elif num > randomnum:
    i+=1
    return 'down'
  else :
    i+=1
    return '정답입니다'

while True:
  a = int(input("숫자를 입력해주세요"))
  b = updown(a)
  if b == '정답입니다':
    print(b,"횟수:",i)
    break
  print(b)
