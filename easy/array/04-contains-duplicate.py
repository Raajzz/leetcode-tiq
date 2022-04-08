# 2 METHODS, use an inbuilt method which uses binary search tree 
# Or, create your own binary search tree

# USING DICTIONARY IN PYTHON

nums = [1,2,3,4]
check_dup = {}

def check_duplicates():
  for element in nums:
    try:
      if(check_dup[element]):
        return False
    except:
      check_dup[element] = 1
  return True

print(check_duplicates())