import random
def seperator():
    print('---'*60)
'''Task1'''
colors=['red','blue','white','yellow','purple','green']
print(random.choice(colors))
seperator()
'''Task2'''
list=[3,5,8,12]
multi=1
for i in list:
    multi*=i
print(multi)
seperator()
'''Task3'''
list=[23,444,5555,12]
print(max(list))
seperator()
'''Task4'''
list=[10,20,30,20,10,50,60,40,80,50,40]
new=[]
for i in list:
    if i not in new:
        new.append(i)
print(new)
seperator()
'''Task5'''
a= [3, 4, 1, 8, -7, 20, 85]
print(sum(a))
seperator()
'''Task6'''
a = [2, 4, 16, 78]
twice = [0, 0, 0, 0]
for i in range(len(a)):
    twice[i]=a[i]*2
print(a)
print(twice)
seperator()
'''Task7'''
a = [2, 45, 66, 80]
b = [23, 444, 1, 90]
sum = [0, 0, 0, 0]
"their size are the same so I don't see difference to write (for) for each list"
for i in range(len(a)):
    sum[i]=a[i]+b[i]
print(sum)
seperator()
'''Task8'''
# creating an empty list
lst = []
n = int(input("Enter number of elements : "))
countEven=0
countOdd=0
# iterating till the range
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
for i in lst:
    if i%2==0:
        countEven+=1
    else: countOdd+=1
print('Even',countEven,'\nOdd',countOdd)
seperator()

'''Task9'''
lst = []
n = int(input("Enter number of elements : "))
negative=[]
positive=[]
# iterating till the range
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
for i in lst:
    if i<0:
        negative.append(i)
    elif i>0:
        positive.append(i)
    else:
        print('zero is neither negative nor positive')
print(negative)
print(positive)
seperator()
'''Task10'''
lst = []
n = int(input("Enter number of elements : "))
newList=[]
# iterating till the range
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
for j in lst:
    if j not in newList:
        newList.append(j)
print(newList)
seperator()