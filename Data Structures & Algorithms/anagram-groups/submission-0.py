from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for i in strs:
            key = ",".join(sorted(i))
            seen[key].append(i)
            
        return list(seen.values())