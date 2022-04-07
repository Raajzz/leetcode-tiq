from unicodedata import digit


digits = [9]

for i in range(len(digits)-1, -1, -1):
  digits[i] += 1
  if(digits[i] == 10):
    digits[i] %= 10
  else:
    break

if(digits[0] == 0):
  digits.insert(0, 1)

print(digits)