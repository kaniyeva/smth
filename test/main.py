import random
a=5
a=[1,2,3,4,5]
a=[1,2.36,'dh',True,[1,2,3]]

mylist=['apple','milk','cheese','icecream','lemonade','tea']
print(len(mylist)) #num of elements
print(mylist[0])#1ft element
print(mylist[-1])#last element
print(mylist[1:3])#take range of elements
print(mylist[1:4:2])# (from : to : step)
print(mylist.append('sushi')) #add new element
print(mylist)
mylist.insert(2,'pizza')#add element by index
print(mylist)
del mylist[0] #deleting element by index
print(mylist)
mylist.remove('icecream')
print(mylist)
mylist[-2]='coffee'
print(mylist) #replace element by index

"""
for i in mylist:
    print(i)#element of list
"""
"""a=0
product=input('Product: ')
for i in range(len(mylist)): #this is index of list
    if mylist[i]==product:
        print(i,mylist[i])
        a=1
if a==0:
    print('NOT FOUND')"""

product=input('Product: ')
if product in mylist:
    print('yes')
else: print('no')



b=[-3,4,5,2,3,6,7,54,89,85,1]
countEven=0
for i in b:
    b.count(i%2==0)
"""
print(max(b)) #maximum of array
print(min(b))
print(sum(b)) #sum of all elements
b.sort() #sorting and save the state of the list
sorted(b) #sort temporary
print(b)
b.sort(reverse=True)
print(b)
print(b.count(4)) #count how many 4 in list
random.shuffle(b) #рандомно перемешать
print(b)
print(random.choice(b)) #рандомный выбор элемента со списка
"""







