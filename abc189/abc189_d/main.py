#!/usr/bin/env python3

import sys
sys.setrecursionlimit(10**7)

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    
    max_val = pow(2, N+1) - 1
    sub = 0
    
    for i, s in enumerate(S, 1):
        if s == "AND":
            sub += pow(2, i)
    
    ans = max_val - sub
    print(ans)
        

if __name__ == '__main__':
    main()