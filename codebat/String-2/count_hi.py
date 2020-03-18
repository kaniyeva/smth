def count_hi(str):
   sum = 0
   for i in range(len(str)-1):
     if (str[i] == "h" and str[i+1] == "i"):
       sum +=1
   return sum
