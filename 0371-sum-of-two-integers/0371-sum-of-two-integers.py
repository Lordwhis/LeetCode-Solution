class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK, MAX = 0xFFFFFFFF, 0x7FFFFFFF
        while b & MASK:
            carry = a & b
            a = a ^ b
            b = carry << 1
        a &= MASK
        return a if a <= MAX else ~(a ^ MASK)