#!/usr/bin/env python3

import sys
sys.setrecursionlimit(10**7)
import math

def factrization_prime(number):
    factor = {}
    div = 2
    s = math.sqrt(number)
    while div < s:
        div_cnt = 0
        while number % div == 0:
            div_cnt += 1
            number //= div
        if div_cnt != 0:
            factor[div] = div_cnt
        div += 1
    if number > 1:
        factor[number] = 1
    return factor

def main():
    N = int(input())
    
    res = factrization_prime(2*N)
    
    ans = 1
    flag = True
    for key, val in res.items():
        if key == 2:
            ans *= 2
        else:
            ans *= (val+1)
            
    print(ans)
            
    


if __name__ == '__main__':
    main()