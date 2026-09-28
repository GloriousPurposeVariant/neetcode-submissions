from collections import defaultdict

    
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_len = 0
        counts = defaultdict(int)

        for r in range(len(s)):

            counts[s[r]] += 1

            while (r - l + 1) - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1


            max_len = max(max_len, r - l + 1)

        return max_len