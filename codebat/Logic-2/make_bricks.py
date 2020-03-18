def make_bricks(small, big, goal):
   if (goal//5 <= big) and ((goal - 5*(goal//5))<= small):
     return True
   elif (goal//5 >= big) and ((goal - 5*(big)) <= small):
     return True
   return False
