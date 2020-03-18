def caught_speeding(speed, is_birthday):
   if is_birthday:
     if (speed <=65):
       return 0
     elif (speed <=85 and speed >=66):
       return 1
     elif speed >= 86:
       return 2
   elif speed <= 60:
     return 0
   elif speed in range(61, 81):
     return 1
   else:
     return 2
