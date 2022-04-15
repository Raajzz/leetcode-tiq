s = "aabb"

store_char = {}

for char in s:
    try:
        store_char[char] += 1
    except:
        store_char[char] = 1

pos_counter = 0

for key in s:
    if(store_char[key] == 1):
        break
    else:
        pos_counter += 1

print (pos_counter if (pos_counter < len(s)) else -1)