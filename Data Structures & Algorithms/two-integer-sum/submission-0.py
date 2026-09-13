class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_map = defaultdict(list)
        for index, value in enumerate(nums):
            val_to_search = target - value
            if val_map[val_to_search]:
                val_map[val_to_search].append(index)
                return val_map[val_to_search]
            val_map[value].append(index)

