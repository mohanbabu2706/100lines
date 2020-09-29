while True:
    print("Enter -1 for exit.")
    num=int(input("enter a number:"))
    if num==-1:
        break
    else:
        number=float(num)
        number_sqrt=number**5
    print("Square root of %0.2f is %0.2f"%(number,number_sqrt))
