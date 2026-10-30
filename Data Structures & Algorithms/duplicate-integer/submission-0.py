class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        trace = set()
        for num in nums:
            if num not in trace:
                trace.add(num)
            else:
                return True
        return False
        