def twoSum(numbers, target):
    l,r=0,len(numbers)-1
    while l<r:
        curr_sum=numbers[l]+numbers[r]
        if curr_sum==target:
            return [l+1,r+1]
        elif curr_sum>target:
            r-=1
        else:
            l+=1
print(twoSum([2,7,11,15],9))
print(twoSum([-1,0],-1))