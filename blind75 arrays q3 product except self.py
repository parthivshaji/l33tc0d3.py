def productExceptSelf(nums):
    products = [1] * len(nums)
    p = 1
    
    for i in range(len(nums)):
        products[i] = p
        p *= nums[i]
        
    p = 1
    
    for i in range(len(nums)-1,-1,-1):
        products[i] *= p
        p *= nums[i]
    
    return products

    