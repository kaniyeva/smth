b=[-3,4,5,2,3,6,7,54,89,85,1]
countEven=0
countOdd=0
for i in b:
    if i%2==0:
        countEven+=1
    else:
        countOdd+=1
print('Odd:',countOdd,'\nEven:',countEven)