def rotate_left3(nums):
   s = []
   temp = nums[0]
   for i in range(1,3):
     s.append(nums[i])
   s.append(temp)
   return s
