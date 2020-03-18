def max_end3(nums):
   maxi = max(nums[0], nums[2])
   for i in range(len(nums)):
     nums[i] = maxi
   return nums
