def array_front9(nums):
  newnums = nums[0:4]
  
  for i in newnums:
    if i == 9:
      return True
  else:
    return False