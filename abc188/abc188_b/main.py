#!/usr/bin/env python3

import sys
sys.setrecursionlimit(10**7)

def main():
    N = int(input())
    A = tuple(map(int, input().split()))
    B = tuple(map(int, input().split()))
    
    result = 0
    for a, b in zip(A, B):
        result += a*b
    
    if result == 0:
        print("Yes")
    else:
        print("No")
    


if __name__ == '__main__':
    main()