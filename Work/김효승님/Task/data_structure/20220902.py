
''' 1 차 테스트
def arithmetic(list):
    count = len(list)
    test= ['+','-','/','*']
    for i in range(0,count,1):
        if list[i] in test:   
            yield i
            

def calcu(num):
    result = 0
    conver = 0

    for j in arithmetic(num):
       print(num[int(arithmetic(num))])

num = list(input())
calcu(num)

'''

# 사칙연산 인덱스 구하기
from re import A


def arithmetic(list,count):
    sign=[]
    test= ['+','-','/','*']
    for i in range(0,count,1):
        if list[i] in test:   
            sign.append(int(i))
    return sign

# 숫자 나누기
def convers(num):
    count = len(num)
    numberring = []
    conver = 0
    for k in count:
        if k.isdigit():
            conver+=k
        else:
            numberring.append(int(conver))
    numberring.append(int(conver))
    return numberring
'''
#계산하기
def calcu(nums):
    number=convers(nums)
    arithm=arithmetic(nums)
    result = 0
    for i in range(0,len(number),2): 
        for j in arithm:
            if nums[j]=='*' or '%':
                if nums[j]=='*':
                    result = number[i] * number[i+1]
                elif nums[j] == '%':
                    result = number[i] % number[i+1]
            elif
'''

nums = list(input())
a =[]
a.append(int(5))
a.append('+')
a.append(int(6))
print(a)