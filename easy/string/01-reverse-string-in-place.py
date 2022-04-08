# NOT COMPLETED #

x = -123

s = list(str(x))

min_flag = 0

try:
    s.remove('-')
    min_flag = 1
except:
    pass

len_s = len(s)

for i in range(int(len_s/2)):
    s[i], s[len_s - 1 - i] = s[len_s - 1 - i], s[i]

s = "".join(s)
print((-int(s) if min_flag == 1 else int(s)) + 1)