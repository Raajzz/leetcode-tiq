nums = [1,1,2]

len_nums = len(nums)
res_counter = 0
if(len(nums) <= 1):
    print(1)
else:
    i = 0
    j = 1
    while( j < len_nums ):
        if( nums[i] != nums[j] ):
            res_counter += 1
            i += 1
            nums[i] = nums[j]
        j += 1

print(res_counter + 1)
print(nums)