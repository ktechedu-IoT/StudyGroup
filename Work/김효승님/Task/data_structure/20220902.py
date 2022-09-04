#공백 제거 및 오류 코드
def Blank(nums):
    remove_set=' '
    blank=[i for i in nums if i not in remove_set]
    for j in blank:
        if j.isalpha():
           return 'a'
    for k in range(0,len(blank),1):
        if blank[k]=='/' and blank[k+1]=='0':
            return 'b'
    
    return blank

# 사칙연산 구하기
def arithmetic(list):
    count = len(list)
    sign=[]
    test= ['+','-','/','*']
    for i in range(0,count,1):
        if list[i] in test:   
            sign.append(list[i])
    return sign

# 숫자 나누기
def convers(num):
    numberring = []
    conver = ''
    for k in num:
        if k.isdigit():
            conver+=k
        else:
            numberring.append(int(conver))
            conver=''
    numberring.append(int(conver))
    return numberring

#계산하기
def calcu(nums):
    blank=Blank(nums)
    if blank=='a':
        return "non-numeric value Error"
    elif blank=='b':
        return "divided by zero Error"
    number=convers(blank)
    arithm=arithmetic(blank)
    result=0
    j=0
    k=0
    if k ==0 :
        for i in range(0,len(arithm),1): 
            if arithm[i]=='*' or '/' :
                if arithm[i]=='*':
                    result = number[i] * number[i+1]
                    number.pop(i+1)
                    number.pop(i)
                    arithm.pop(i)
                    k+=1
                    break
                elif arithm[i] == '/':
                    result = number[i] / number[i+1]
                    number.pop(i+1)
                    number.pop(i)
                    arithm.pop(i)
                    k+=1
                    break
    if k ==0 :
        for i in range(0,len(arithm),1): 
            if k==0 and arithm[i]=='+' or '-' :
                if arithm[i]=='+':
                    result = number[i] + number[i+1]
                    number.pop(i+1)
                    number.pop(i)
                    arithm.pop(i)
                    k+=1
                    break
            elif arithm[i] == '-':
                result = number[i] - number[i+1]
                number.pop(i+1)
                number.pop(i)
                arithm.pop(i)
                k+=1
                break
    while not number==[] and k==1:
        if arithm[j]=='*':
            result *=number[j]
            number.pop(j)
            arithm.pop(j)
        elif arithm[j] == '/':
            result /= number[j]
            number.pop(j)
            arithm.pop(j)
        elif arithm[j] == '+':
            result += number[j]
            number.pop(j)
            arithm.pop(j)
        elif arithm[j] == '-':
            result -= number[j]
            number.pop(j)
            arithm.pop(j)
        j+=1
    if type(result)==float:
        return int(result * (10**4))/(10**4)
    return result
        
num = input()
result = calcu(num)
print(result)


