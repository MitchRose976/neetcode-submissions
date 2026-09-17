class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = defaultdict(int)
        for n in nums:
            num_count[n] = num_count[n] + 1

        most_frequent = sorted(num_count, key=lambda x: num_count[x], reverse=True)[:k]
        return most_frequent
        
        