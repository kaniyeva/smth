def cigar_party(cigars, is_weekend):
   if (cigars in range(40, 61)):
     return True
   elif (is_weekend and cigars >=40):
       return True
   else:
     return False
