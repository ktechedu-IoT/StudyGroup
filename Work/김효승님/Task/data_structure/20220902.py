
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

''' 2차 
# 사칙연산 인덱스 구하기
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

#우선순위
def Priority(nums):
    sign = arithmetic(nums)
    resize=[]
    for i in sign:
            if nums[i]=='*':
                resize.append(i)
            elif nums[i] == '/':
                resize.append(i)]
    for i in sign:
        if resize not in sign
            resize.append(i)
#계산하기
def calcu(nums):
    number=convers(nums)
    arithm= Priority
    result = 0
    for i in range(0,len(number),2): 
        for j in arithm:
            if nums[j]=='*' or '%':
                if nums[j]=='*':
                    result = number[i] * number[i+1]
                elif nums[j] == '/':
                    result = number[i] / number[i+1]
            elif

'''
#수정 필요사항
#사칙연산 수정시 숫자 순서 맞춰서 변경이 필요 (해결시 패턴 5)
#패턴 7 8 숫자 나누기에서 처리 하기