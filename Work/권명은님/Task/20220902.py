def calculator(datas:list):
    dataList = sep(datas)
    rtn = 0
    cal = ['+', '-', '/', '*']

    if len(dataList) != 3 or dataList[1] not in cal:
        print("non-numeric value Error")
        return

    if dataList[1]=='+':
        rtn = dataList[0]+dataList[2]
    elif dataList[1]=='-':
        rtn = dataList[0]-dataList[2]
    elif dataList[1]=='*':
        rtn = dataList[0]*dataList[2]
    elif dataList[1]=='/':
        if dataList[2] == 0:
            print("divided by zero Error")
            return
        else:
            rtn = dataList[0]//dataList[2] if int(dataList[0]/dataList[2])==dataList[0]/dataList[2] else f'{dataList[0]//dataList[2]:0.4f}'
    return rtn
            
def sep(datas:str):
    datas = datas.replace(' ', '') #공백제거
    dataList = []
    tmp = ''
    for data in datas:
        if data.isdecimal():
            tmp += data
        else:
            if tmp.isdecimal():
                dataList.append(int(tmp))
            dataList.append(data)
            tmp = ''
    if tmp:
        dataList.append(int(tmp))
    return dataList

datas = input("계산식을 입력해주세요. >>")
result = calculator(datas)
if result:
    print(result)

