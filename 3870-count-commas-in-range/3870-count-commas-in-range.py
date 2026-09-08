class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0

        for i in range(1, n + 1):
            x = i

            while x >= 1000:
                ans += 1
                x //= 1000

        return ans