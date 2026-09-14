class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        op = 0

        while num > 0:
            rem = num % 10
            op = op * 10 + rem
            num //= 10

        return op == x    