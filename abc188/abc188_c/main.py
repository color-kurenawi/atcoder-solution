#!/usr/bin/env python3

import sys
sys.setrecursionlimit(10**7)
    

def main():
    N = int(input())
    A = tuple(map(int, input().split()))
    
    def dfs(depth, idx):
        if depth == N:
            return idx
        else:
            left_idx = dfs(depth+1, idx)
            right_idx = dfs(depth+1 , idx + 2**(N- 1 - depth))
            
            if A[left_idx] > A[right_idx]:
                winner = left_idx
                loser = right_idx
            else:
                winner = right_idx
                loser = left_idx
            
            if depth == 0:
                return loser
            else:
                return winner
    
    ans = dfs(0, 0) + 1
    print(ans)
            
            


if __name__ == '__main__':
    main()