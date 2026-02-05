from typing import List
def twoSum(nums: List[int], target: int) :
    hash_map = {}
    for i in range(len(nums)):
        hash_map[nums[i]] = i
    
    for j in range(len(nums)):
        complement = target - nums[j]
        if (complement in hash_map and hash_map[complement]!= j):
            return [j,hash_map[complement]]
        

arr = [3,2,4]
print(twoSum(arr,6))

        