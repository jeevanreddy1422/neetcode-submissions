class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        r = [0] * (2*n)
        for i,num in enumerate(nums):
            r[i] = r[i+n] =num
        return r
        