class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            left_letter = s[l]
            right_letter = s[r]

            if not left_letter.isalnum():
                l += 1
            elif not right_letter.isalnum():
                r -= 1
            elif left_letter.lower() != right_letter.lower():
                return False

            else:
                l += 1
                r -= 1

        return True