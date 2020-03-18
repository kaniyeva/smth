def extra_end(str):
   result = ""
   for i in range(3):
      result+=str[len(str)-2:len(str)]
   return result
