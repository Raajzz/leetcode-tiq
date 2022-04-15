
nums1 = [1,2,2,1]
nums2 = [2,2]

store_elem = {}

for element in nums1:
  try:
    store_elem[element] += 1
  except:
    store_elem[element] = 1

output = []

for element in nums2:
  try:
    if(store_elem[element]):
      output.append(element)
      store_elem[element] -= 1
  except:
    pass

print(output)