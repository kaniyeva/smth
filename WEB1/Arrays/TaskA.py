n=int(input())
a=[int(i) for i in input().split()]
for j in range(len(a)):
    if j%2==0:
        print(a[j],end=' ')


