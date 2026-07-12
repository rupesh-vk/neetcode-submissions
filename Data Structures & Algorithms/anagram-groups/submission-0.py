class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #create a signature, by sorting the first
        #str in strs and then use it to check, you have
        #to check and append the similar pattern

        output = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))


            output[key].append(s)

        return list (output.values())
        