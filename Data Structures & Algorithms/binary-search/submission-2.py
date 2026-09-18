class Solution:
    def search(self, nums: List[int], target: int) -> int:
        middle_index = len(nums) // 2
        print(f"middle_index {middle_index}")

        if nums[middle_index] == target:
            return middle_index

        new_list = []
        offset = 0
        if nums[middle_index] < target:
            new_list = nums[middle_index:]
            offset = len(nums) - len(new_list)
        
        if nums[middle_index] > target:
            new_list = nums[:middle_index]

        for index, num in enumerate(new_list):
            if num == target:
                return index + offset

        return -1
