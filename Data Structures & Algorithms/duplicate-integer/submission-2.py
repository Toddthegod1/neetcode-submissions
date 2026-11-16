class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        stored = set()
        for i in nums:
            if i in stored:
                return True
            stored.add(i)
        return False