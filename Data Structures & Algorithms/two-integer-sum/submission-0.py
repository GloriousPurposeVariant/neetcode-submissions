class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            to_look = target - num
            if to_look in seen:
                return [seen.get(to_look), i]
            else:
                seen[num] = i