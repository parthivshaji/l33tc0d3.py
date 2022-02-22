def maxProfit(prices):
    left_pointer = 0
    right_pointer = 1
    maxP = 0
    
    while right_pointer < len(prices):
        #checking if profitable
        if prices[left_pointer] < prices[right_pointer]:
            profit = prices[right_pointer] - prices[left_pointer]
            maxP = max(maxP,profit)
        else:
            left_pointer = right_pointer
        right_pointer += 1
    return maxP

print(maxProfit([7,1,5,3,6,4]))