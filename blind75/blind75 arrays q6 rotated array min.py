def findMin(nums):
    res = nums[0]
    left = 0
    right = len(nums)-1
    
    while left<=right:
        if nums[left] < nums[right]:
            res = min(res,nums[left])
            break
        middle = (left + right)//2
        res = min(res,nums[middle])
        if nums[middle] >= nums[left]:
            left = middle + 1
        else:
            right = middle - 1
    
    return res