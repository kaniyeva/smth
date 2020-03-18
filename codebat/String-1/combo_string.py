def combo_string(a, b):
   short = min(len(a), len(b))
   if (len(a) == short):
     return a+b+a
   else:
     return b+a+b
