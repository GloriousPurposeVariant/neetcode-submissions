class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(w)}#{w}" for w in strs)
            
        
    def decode(self, s: str) -> List[str]:
        i, j = 0, 0
        words = []
        while j < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            word = s[j + 1: j + 1 + length]
            words.append(word)
            i = j + 1 + length
            j = i
        return words   