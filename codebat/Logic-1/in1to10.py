def in1to10(n, outside_mode):
   if(n>1 and n<10):
     return not outside_mode
   else:
     return outside_mode or n is 10 or n is 1
