n=int(input())
list=[int(i) for i in input().split()]
ans='NO'
for i in range(1,len(list)):
    if (list[i]>=0 and list[i-1]>=0) or (list[i]<0 and list[i-1]<0):
        ans='YES'
print(ans)

