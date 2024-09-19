class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        mother = 1
        son = 1
        if n == 1 or m ==1:
            return 1
        if n == 0 or m ==0:
            return 0
        if m >= n:
            for i in range(m, m+n-1, 1):
                mother = mother * (m+n-1-i)
                son = son*i
        else:
            for i in range(n, m+n-1, 1):
                mother = mother * (m+n-1-i)
                son = son*i
        return son//mother