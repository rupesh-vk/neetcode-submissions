class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #top k frequent elements

        #Build hasmap to count the frequency of each number
        #create a bucket array with frequency, so every element that has the same
        #frequency goes into the specific bucket.
        #After filling, I will iterste from highest frequency to lowest. collecting
        #nummebrs until I have k of them
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        freq = [[] for _ in range(len(nums) + 1)]

        for num, c in count.items():
            freq[c].append(num)
        
        res = []
        for i in range(len(freq)-1, 0 , -1):
            for num in freq[i]:
                res.append(num)

                if len(res) == k:
                    return res
                    
        