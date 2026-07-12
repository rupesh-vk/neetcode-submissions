class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #create a seen map, to check the target

        seen = {} #to store key -> value pair
        for i,n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [seen[diff], i]
            else:
                seen[n] = i

        