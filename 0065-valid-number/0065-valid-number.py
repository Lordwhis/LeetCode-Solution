class Solution:
    def isNumber(self, s: str) -> bool:
        n = len(s)
        i = 0
        
        if i < n and s[i] in "+-":
            i += 1

        digits_before = 0
        while i < n and s[i].isdigit():
            digits_before += 1
            i += 1

        if i < n and s[i] == '.':
            i += 1

        digits_after = 0
        while i < n and s[i].isdigit():
            digits_after += 1
            i += 1

        if digits_before + digits_after == 0:
            return False

        if i < n and s[i] in "eE":
            i += 1

            if i < n and s[i] in "+-":
                i += 1

            exp_digits = 0
            while i < n and s[i].isdigit():
                exp_digits += 1
                i += 1

            if exp_digits == 0:
                return False
        return i == n
