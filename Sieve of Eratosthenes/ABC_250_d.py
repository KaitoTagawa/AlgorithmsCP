from sys import stdin
from math import gcd, floor, ceil
input = stdin.readline

"""https://atcoder.jp/contests/abc250/tasks/abc250_d"""
"""
    Though process:
    Can rephrase the question to: If N >= p * q^3 is satisfied (p,q) is similar to 250.
    How many (p,q) pairs are there?
    Answer:
    Rewrite the formula as N/p >= q^3. Starting from largest q < N, find how many p satisfies the formula?
    Use sieve of eratosthenes to find primes (p,q). Note we only need prime of up to 10^6.
    Once q is selected, narrow down the p using binary search.
"""



def main():
    n = int(input())
    if n < 3:
        print(0)
        return
    # find primes up to rootcube(n) with sieve of eratosthenes
    maxLim = ceil(n**(1/3))
    isPrime = set(i for i in range(maxLim))
    isPrime.remove(0)
    isPrime.remove(1)
    for i in range(2, maxLim):
        if i not in isPrime:
            continue
        for j in range(i * 2, maxLim, i):
            if j in isPrime:
                isPrime.remove(j)

    isPrime = list(isPrime)
    ans = 0
    for j,i in enumerate(isPrime):
        n_i = n/i
        # Binary search
        l = -1
        r = len(isPrime)
        while l + 1 < r:
            m = (l + r) // 2
            q = isPrime[m]
            if q**3 > n_i:
                r = m
            else:
                l = m
        if l > j:
            ans += l - j
    print(ans)




main()