
def twoSum(nums, target):
    hashmap = {}
    for i,j in enumerate(nums):
        diff = target - j
        if diff in hashmap:
            return [hashmap[diff],i]
        hashmap[j] = i

print(twoSum([2,7,11,15],9))


