class Solution:
    def fib(self, n: int) -> int:
        store = [-1] * (n + 1)
        def fib_memo(n: int) -> int:
            if n <= 1:
                return n
            store[n] = (store[n] if store[n] != -1 else fib_memo(n - 1) + fib_memo(n - 2))
            return store[n]

        return fib_memo(n)