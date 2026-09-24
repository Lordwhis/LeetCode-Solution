class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            temp = str(nums[i])
            t = 0

            for s in temp:
                t += int(s)

            if t == i:
                return i

        return -1