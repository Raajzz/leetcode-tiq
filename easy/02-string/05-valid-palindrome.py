s = "0S0"

new_string = ""
for char in s:
    if(char.isalpha()):
        new_string += char.lower()
    elif(char.isdigit()):
        new_string += char
        
len_new_string = len(new_string)

if(len_new_string <= 1):
    print(True)
else:
    for i in range(int(len(new_string)/2)):
        if(new_string[i] != new_string[len_new_string - 1 - i]):
            print(False)
            exit()
    print(True)