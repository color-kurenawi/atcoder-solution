#!/usr/bin/env python3

import sys
sys.setrecursionlimit(10**7)

def main():
    N, M = map(int, input().split())
    
    def int0(s): return int(s) - 1
    
    conds = [tuple(map(int0, input().split())) for _ in range(M)]
    
    K = int(input())
    info = [tuple(map(int0, input().split())) for _ in range(K)]
    
    def calc(s):
        balls = [0]*N
        for (c, d), flag in zip(info, s):
            if flag == "l":
                balls[c] += 1
            else:
                balls[d] += 1

        res = 0
        for a, b in conds:
            if balls[a] and balls[b]:
                res += 1
        return res
                
    def dfs(s):
        if len(s) == K:
            res = calc(s)
            return res
        else:
            left = dfs(s+"l")
            right = dfs(s+"r")
            return max(left, right)
    
    ans = dfs("")
    print(ans)
            


if __name__ == '__main__':
    main()