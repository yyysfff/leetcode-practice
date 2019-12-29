def twoSum( nums, target):
    List=[]
    num_sort=sorted(nums)
    num_re=nums[:]
    i=0
    while(num_sort[i]<=target/2):
        if num_sort[i]==target-num_sort[i]:
            num_re.remove(num_sort[i])
            if target-num_sort[i] in num_re:
                List.append(nums.index(num_sort[i]))
                List.append(num_re.index(target-num_sort[i])+1)
                break
        if target-num_sort[i] in nums:
            List.append(nums.index(num_sort[i]))
            List.append(nums.index(target-num_sort[i]))
            break
        i+=1
    return List

a=twoSum([3,2,3],6)
print(a)
