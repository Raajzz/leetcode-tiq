s = "rat"
t = "tar"

store_char = {}

def fun_anagram(s, t):
    if(len(s) != len(t)):
        return False

    for char in s:
        try:
            store_char[char] += 1
        except:
            store_char[char] = 1

    for char in t:
        try:
            store_char[char] -= 1
            if(store_char[char] < 0):
                return(False)
        except:
            return False

    return(True)

print(fun_anagram("ab", "a"))