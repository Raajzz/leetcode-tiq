# TIME LIMIT EXCEEDED

k = 2
nums = [-1,-100,3,99]
len_nums = len(nums)

counter = 0
while(counter < k):
  last_elem = nums[len_nums-1]
  for i in range(len_nums-1, 0, -1):
    nums[i] = nums[i-1]
  nums[0] = last_elem
  counter += 1
print(nums)

# SWAPPING - INCOMPLETE