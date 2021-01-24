#!/usr/bin/env python3

import numpy as np

import sys
def read():return sys.stdin.buffer.read()
def readline():return sys.stdin.buffer.readline()
def readlines():return sys.stdin.buffer.readlines()

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

def cc_export():
    from numba.pycc import CC
    cc = CC('my_module')
    cc.export('solve', 'i8(i8, i8[:])')(solve)
    cc.compile()
    

if __name__ == '__main__':
    try:
        from my_module import solve
    except:
        if sys.argv[-1] == 'ONLINE_JUDGE':
            cc_export()
        from my_module import solve
    main()