import math
def seperator():
    print('---'*60)
#Task1
lst = []
n = int(input("Enter number of elements : "))
firstList=[]
lastList=[]
# iterating till the range
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
for j in lst[0,6]:
    root=math.sqrt(j)
    if j not in firstList and int(root**2)==j:
        firstList.append(j)
for k in lst[-1,-6]:
    if k not in lastList:
        lastList.append(k)
print(firstList)
print(lastList)


seperator()
#Task2
seperator()
#Task3
seperator()
#Task4
seperator()
#Task5
seperator()
#Task6
seperator()
#Task7
seperator()
#Task8
seperator()
#Task9
seperator()
#Task10
seperator()

