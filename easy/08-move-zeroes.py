# TWO POINTER METHOD, WHERE ONE POINTER WOULD BE FOR ZEROS AND THE
# OTHER FOR NON ZEROS

# nums = [1,0]

# nzp = 0
# zp = 0

# while(True):
#     while(nums[nzp] != 0):
#         nzp += 1
#         if(nzp >= len(nums)):
#             break
#     while(nums[zp] == 0):
#         zp += 1
#         if(zp >= len(nums)):
#             break
#     if(zp >= len(nums) or nzp >= len(nums)):
#         break
#     if(zp > nzp):
#         nums[nzp], nums[zp] = nums[zp], nums[nzp]
#     else:
        

# print(nums)

# ---------------------------------------------------------------

nums = [1,0]

ptr_0 = 0
ptr_1 = ptr_0

while(True):
    while(ptr_0 < len(nums) and nums[ptr_0] != 0):
        ptr_0 += 1
    ptr_1 = ptr_0
    while(ptr_1 < len(nums) and nums[ptr_1] == 0):
        ptr_1 += 1
    if(ptr_0 < len(nums) and ptr_1 < len(nums)):
        nums[ptr_0], nums[ptr_1] = nums[ptr_1], nums[ptr_0]
    else:
        break

print(nums)