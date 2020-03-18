n=int(input())
list=[int(i) for i in input().split()]
for i in range(len(list)//2):
    newOne=list[i]
    list[i]=list[len(list)-i-1]
    list[len(list) - i-1]=newOne

for i in range(len(list)):
    print(list[i])