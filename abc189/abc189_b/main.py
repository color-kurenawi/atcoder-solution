#!/usr/bin/env python3

import sys
sys.setrecursionlimit(10**7)

def main():
    N, X = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(N)]
    
    
    amount = 0
    ans = -1
    for i, (v, p) in enumerate(info):
        amount += v * p
        if amount > X*100:
            ans = i+1
            break
    
    print(ans) 


if __name__ == '__main__':
    main()