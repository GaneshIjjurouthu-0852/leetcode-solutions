def two_sum(nums,target):
    history={}
    for i in range(len(nums)):
        need=target-nums[i]
        if need not in history:
            history[nums[i]]=i
        else:
            return [history[need],i]
print(two_sum([2,7,11,15],9))