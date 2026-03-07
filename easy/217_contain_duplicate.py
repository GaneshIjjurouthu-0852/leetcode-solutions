def contain_dup(nums):
    seen=set()
    for i in nums:
        if i in seen:
            return True
        seen.add(i)
    return False
print(contain_dup([1,2,3,4]))