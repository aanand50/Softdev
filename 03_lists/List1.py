def first_last6(nums):
  if nums[0] == 6:
    return True
  if nums[len(nums)-1]==6:
    return True
    
  return False


def same_first_last(nums):
  if len(nums) >= 1:
    if nums[0] == nums[-1]:
      return(True)
    else:
      return(False)
  else:
    return(False)


def make_pi():
  a = [3, 1, 4]
  return(a)


def common_end(a, b):
  if a[0]==b[0] or a[-1]==b[-1]:
    return(True)
  else:
    return(False)



def has23(nums):
  return(2 in nums or 3 in nums)
