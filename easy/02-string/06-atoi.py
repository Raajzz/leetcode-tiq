"""
1. Ignore whitespaces => trim 
2. '-' or '+' and figure out whether negative or positive
3. read until a non digit character is reached
4. "123" -> 1 and then 2 and then 3

"""

s = "words and 987"

res = "0"

sign_flag = 0 
# 0 means positive
# 1 means negative

# for whitespace
store_break = 0
for counter in range(len(s)):
    if(s[counter] == '-'):
        sign_flag = 1
    elif(s[counter] == '+'):
        sign_flag = 0
    elif(s[counter].isspace()):
        pass
    else:
        store_break = counter
        break

for counter in range(store_break, len(s)):
    if(s[counter].isdigit()):
        res += s[counter]
    else:
        break

res_int = (-int(res)) if (sign_flag == 1) else (int(res))

if(res_int < -2147483648):
    print(-2147483648)
elif(res_int > 2147483647):
    print(2147483647)
else:
    print(res_int)