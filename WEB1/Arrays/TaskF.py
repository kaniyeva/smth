n=int(input())
count=0
list=[int(i) for i in input().split()]
length=len(list)-1
for i in range(1,length):
    if (list[i]>list[i-1] and list[i]>list[i+1]):
        count+=1
print(count)