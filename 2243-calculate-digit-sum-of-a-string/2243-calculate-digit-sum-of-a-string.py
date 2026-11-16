class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            temp = ""
            c = 0
            t = 0

            for i in s:
                t += int(i)
                c += 1

                if c == k:
                    temp += str(t)
                    c = 0
                    t = 0

            if c > 0:
                temp += str(t)

            s = temp

        return s              
