class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        index = 0
        n = len(nums)

        for i in range(n):
            if n % (i + 1) == 0:
                index += nums[i] * nums[i]
        return index