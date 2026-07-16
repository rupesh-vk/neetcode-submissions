class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #so we do two passes and fill a prefix and suffix
        #subarray, that will give us product of array
        #except self

        result = [1] * len(nums)
        #prefilled an ouptut array

        #sample : [1,2,3,4]
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

            #result = [1, 1, 2, 6]

        suffix = 1
        for i in range(len(nums)-1,-1,-1): #[1,2,3,4]
            #we iterate from back to get the suffix value
            result[i] *= suffix #[-, -, -,6]
            suffix *= nums[i] 

        return result 
        