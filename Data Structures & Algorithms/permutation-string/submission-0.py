from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2): return False

        k = len(s1)
        s1_map = defaultdict(int)
        s2_map = defaultdict(int)

        for l in s1:
            s1_map[l] += 1

        for l in s2[:k]:
            s2_map[l] += 1

        if s1_map == s2_map: return True

        for r in range(k, len(s2)):
            s2_map[s2[r]] += 1

            outgoing = s2[r - k]

            s2_map[outgoing] -= 1
            if s2_map[outgoing] <= 0:
                del s2_map[outgoing]

            if s1_map == s2_map: return True

        return False