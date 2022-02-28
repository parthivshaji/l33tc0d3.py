def maxProduct(nums):
    maxProd = max(nums)
    curMin, curMax = 1, 1
    
    for i in nums:
        if i == 0:
            curMin, curMax = 1, 1
            continue
        tmp = curMax * i    
        curMax = max(i * curMax, i * curMin, i)
        curMin = min(tmp, i * curMin, i)
        maxProd = max(maxProd,curMax)
    return maxProd