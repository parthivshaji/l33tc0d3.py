def maxSubArray(nums):
    maxSub = nums[0]
    sumt = 0
    for i in range(len(nums)):
        if sumt < 0:
            sumt = 0
        sumt += nums[i]
        maxSub = max(maxSub,sumt)
    return maxSub