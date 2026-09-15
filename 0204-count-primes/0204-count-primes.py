class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        is_prime=[True]*n
        is_prime[0]=False
        is_prime[1]=False
        i=2
        while i*i<n:
            if is_prime[i]:
                is_prime[i*i:n:i]=[False]*(((n-1-i*i)//i)+1)
            i+=1
        return sum(is_prime)
        