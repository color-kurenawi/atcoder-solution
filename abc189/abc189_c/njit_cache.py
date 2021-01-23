#!/usr/bin/env python3

import numpy as np
from numba import njit, i8

import sys
def read():return sys.stdin.buffer.read()
def readline():return sys.stdin.buffer.readline()
def readlines():return sys.stdin.buffer.readlines()

@njit(i8(i8, i8[:]), cache=True)
def solve(N, A):
    ans = np.zeros(1, dtype=np.int64)
    for i in range(N):
        min_val = A[i]
        for j in range(i, N):
            min_val = min(min_val, A[j])
            score = min_val * (j-i+1)
            ans[0] = max(ans[0], score)
    return ans[0]

def main():
    stdin = np.fromstring(read().decode(), dtype=np.int64, sep=" ")
    N = stdin[0]
    A = stdin[1:]
    ans = solve(N, A)
    print(ans)

if __name__ == '__main__':
    main()