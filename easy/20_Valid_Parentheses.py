def isValid(s):
    match={")":"(","]":"[","}":"{"}
    check=[]
    for i in s:
        if i in match.values():
            check.append(i)
            continue
        if not check:
            return False
        item=check.pop()
        if match[i]!=item:
            return False
    return len(check)==0
print(isValid("([)]"))