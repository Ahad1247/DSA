from typing import List

nums = [3,4,5,2]
def maxProduct(nums: List[int]):
    highest = max(nums[0],nums[1])
    second_highest = min(nums[0],nums[1])
    
    for i in range(len(nums)):
        if (highest<=nums[i]):
            second_highest = highest
            highest = nums[i]
        elif (second_highest<=nums[i]):
            second_highest = nums[i]
    
    return ((highest-1)*(second_highest-1))

print(maxProduct(nums))


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        biggest = 0
        second_biggest = 0
        
        for num in nums:
            if num > biggest:
                second_biggest = biggest
                biggest = num
                
            else:
                second_biggest = max(second_biggest, num)
        
        return (biggest - 1) * (second_biggest - 1)
