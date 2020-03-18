def sum2(nums):
   sum = 0
   if (len(nums) <= 2):
     for i in range(len(nums)):
       sum+=nums[i]
   else:
       for i in range(0, 2):
         sum+=nums[i]
   return sum
