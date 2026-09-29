from collections import defaultdict


class Solution:

    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""

        t_map = defaultdict(int)

        for i in t:
            t_map[i] += 1

        l = 0
        min_len = float('inf')
        res = [-1, -1]
        need = len(t_map)
        have = 0

        s_map = defaultdict(int)

        for r in range(len(s)):
            char = s[r]

            s_map[char] += 1

            if char in t_map and s_map[char] == t_map[char]:
                have += 1

            while have == need:
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    res = [l, r]
                    
                s_map[s[l]] -= 1

                if s[l] in t_map and s_map[s[l]] < t_map[s[l]]:
                    have -= 1

                l += 1

        start, end = res
        return s[start: end + 1] if min_len != float('inf') else ""