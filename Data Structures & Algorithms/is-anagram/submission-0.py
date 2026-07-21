class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letter_s, letter_t = {}, {}
        
        for i in s:
            if i not in letter_s.keys():
                letter_s[i] = 1
            else:
                letter_s[i] = letter_s.get(i, 0) + 1
        
        for i in t:
            if i not in letter_t.keys():
                letter_t[i] = 1
            else:
                letter_t[i] = letter_t.get(i, 0) + 1
                
        return letter_s == letter_t