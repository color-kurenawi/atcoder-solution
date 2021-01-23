#!/usr/bin/env python3

import sys
sys.setrecursionlimit(10**7)
def input():return sys.stdin.readline().strip()

def main():
    N, C = map(int, input().split())
    info = [tuple(map(int, input().split())) for _ in range(N)]
    
    info_set = set()
    for a, b, c in info:
        info_set.add(a)
        info_set.add(b+1)
    
    dates = sorted(info_set)
    dates_d = {date:idx for idx, date in enumerate(dates)}
    M = len(dates)
        
    imos = [0]*(M+1)
    
    for a, b, c in info:
        a_idx = dates_d[a]
        b_idx = dates_d[b+1]
        imos[a_idx] += c
        imos[b_idx] -= c
    
    cum_sum = [0] * (M+1)
    
    for i in range(M):
        cum_sum[i+1] = cum_sum[i] + imos[i]
    
    ans = 0

    for i in range(M-1):
        add = min(cum_sum[i+1], C) * (dates[i+1] - dates[i])
        ans += add
    print(ans)
    


if __name__ == '__main__':
    main()