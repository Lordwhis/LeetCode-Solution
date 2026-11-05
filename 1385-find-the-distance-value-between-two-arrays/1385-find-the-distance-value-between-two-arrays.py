class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        c = 0

        for i in range(len(arr1)):
            t = 0
            for j in range(len(arr2)):
                temp = abs(arr1[i] - arr2[j])
                
                if temp > d:
                    t += 1
                else:
                     t -= 1
            
            if t == len(arr2):
                c += 1
        
        return c