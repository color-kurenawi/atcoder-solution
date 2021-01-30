#!/usr/bin/env python3

import sys
sys.setrecursionlimit(10**7)

def main():
    N, S, D = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(N)]
    
    ans = "No"
    for x, y in info:
        if x < S and y > D:
            ans = "Yes"
    print(ans)

if __name__ == '__main__':
    main()