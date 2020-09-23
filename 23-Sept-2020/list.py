a=['spam','eggs',100,1234]
print("list a=",a)
#list indices start at 0,
print('a[0]=',a[0])
print('a[3]=',a[3])
print('a[-2]=',a[-2])
#list can be sliced,concated and so on:
print("a[1:-1]=",a[1:-1])
print(a[:2]+['bacon',2*2])
print(3*a[:3]+['Boe!'])
#possible to change individual elements of a list:
a[2]=a[2]+23
print("changing a[2]=",a)
#assingment to slices is also possible,and this can even change the size of the list:
#repkace some items:
a[0:2]=[1,12]
print(a)
#Remove some:
a[0:2]=[]
print(a)
#insert some:
a[1:1]=['bletch','xyzzy']
print(a)
