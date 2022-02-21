def productExceptSelf(nums):
    products = [1] * len(nums)
    # Setting prefix array
    p = 1
    for i in range(len(nums)):
        products[i] = p
        p *= nums[i]

    # Multiplying with postfixes  
    p = 1
    
    for i in range(len(nums)-1,-1,-1):
        products[i] *= p
        p *= nums[i]
    
    return products

