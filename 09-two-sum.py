

nums = []

target = 0

dict_index = {}
dict_pairs = {}

result = []

for counter in range(len(nums)):
    dict_index[nums[counter]] = counter
    dict_pairs[nums[counter]] = target - counter

for item in nums:
    if(dict_pairs[dict_pairs[item]] == item):
        dict_index_1 = dict_index[item]
        dict_index_2 = dict_index[dict_pairs[item]]
        if(dict_index_1 != dict_index_2):
            result.extend(dict_index_1, dict_index_2)

return result