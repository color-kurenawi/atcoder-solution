#!/usr/bin/env python3

import sys
sys.setrecursionlimit(10**7)

def main():
    N = int(input())
    A = tuple(map(int, input().split()))
    
    ans = 0
    for i in range(N):
        min_val = A[i]
        for j in range(i, N):
            min_val = min(min_val, A[j])
            score = min_val * (j-i+1)
            ans = max(ans, score)
    print(ans)
            


if __name__ == '__main__':
    main()