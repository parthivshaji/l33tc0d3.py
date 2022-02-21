def containsDuplicate(nums):
    hashMap = {}
    for i,j in enumerate(nums):
        if j not in hashMap.keys():
            hashMap[j] = 1
        else:
            hashMap[j] += 1
            if hashMap[j] > 1:
                return True
    print(hashMap)
    return False
