def reverse3(a):
   for i in range(len(a)//2):
         temp = a[i]
         a[i] = a[len(a)-i-1]
         a[len(a)-i-1] = temp
   return a
