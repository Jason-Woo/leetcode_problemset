def seperate(str):
    result = []
    i = 0
    while i in range(len(str) - 1):
        if str[i + 1] != '*':
            result.append(str[i])
            i += 1
        else:
            result.append(str[i:i + 2])
            i += 2
    if i < len(str) and str[i] != '*':
        result.append(str[i])
    return result
p=['a','b']
s=['a','a*','.']
tbl = [[False for _ in range(len(p))]for _ in range(len(s))]
print(tbl)


