#!/usr/bin/env python3

import sys
sys.setrecursionlimit(10**7)

def main():
    H, W = map(int, input().split())
    field = [input() for _ in range(H)]
    
    ans = 0
    for i in range(H-1):
        for j in range(W-1):
            count = sum(field[i+k][j+l] == "#" for k in range(2) for l in range(2))
            if count in [1, 3]:
                ans += 1
    
    print(ans)

if __name__ == '__main__':
    main()