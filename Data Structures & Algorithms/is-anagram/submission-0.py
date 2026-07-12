class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        s_dict = {}
        for ch in s:
            if ch in s_dict:
                s_dict[ch] +=1
            else:
                s_dict[ch] = 1
        
        for ch in t:
            if ch in s_dict:
                s_dict[ch] -=1

        for count in s_dict.values():
            if count != 0:
                return False
        return True
        