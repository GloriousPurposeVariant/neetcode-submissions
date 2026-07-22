class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        for i in nums:
            if i not in count_map:
                count_map[i] = 1
            else:
                count_map[i] = count_map.get(i, 0) + 1
                
        count_list = [[] for _ in range(len(nums) + 1)]
        for key, value in count_map.items():
            count_list[value].append(key)
            
        res = []
        for i in range(len(count_list) -1, 0, -1):
            for n in count_list[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        return res