x = -2147483641

neg_flag = 0

if(x < 0):
    neg_flag += 1

x_list = list(str(x))

try:
    x_list.remove('-')
except:
    pass

len_x_list = len(x_list)

for i in range(int(len_x_list/2)):
    x_list[i], x_list[len_x_list-i-1] = x_list[len_x_list-i-1], x_list[i] 

x = -int("".join(x_list)) if neg_flag == 1 else int("".join(x_list))

if(x >= -2147483648 and x<=2147483647):
    print(x)
else:
    print(0)