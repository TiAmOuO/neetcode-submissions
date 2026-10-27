class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()            # record the numbers we've seen
        for n in nums:          # take each number one by one
            if n in seen:       # if n has appeared before
                return True     # duplicate found, stop early
            seen.add(n)         # otherwise, record n
        return False            # checked all, no duplicates