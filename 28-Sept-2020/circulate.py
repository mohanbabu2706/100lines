num = [1,2,3,4,5,6]
def rotate(lst,x):
    if x>=0:
        for i in range(x):
            lastNum=lst.pop(-1)
            lst.insert(0,lastNum)
    else:
        for i in range(abs(x)):
            firstNum=lst.pop(0)
            lst.append(firstNum)
    return
print(num)
rotate(num,2)
print(num)
rotate(num,-2)
print(num)
