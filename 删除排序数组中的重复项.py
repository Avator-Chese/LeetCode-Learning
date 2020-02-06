def fun(s):
    i = 0
    while 1:
        if i+1 < len(s):
            if s[i] != s[i+1]:
                i = i+1
            else:
                del s[i]
        else:
            break
    return len(s), s


print(fun([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
