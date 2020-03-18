def left2(str):
   result = ""
   chars = str[:2]
   if (len(str) > 2):
     result = str[2: len(str)] + chars
   else:
     result = str
   return result
