class Solution:
    def fib(self, n: int) -> int:
        if(n==1):
            return 1
        elif(n==0):
            return 0
        a=self.fib(n-1)
        b=self.fib(n-2)
        return a+b