#!/usr/bin/env python3

import sys
sys.setrecursionlimit(10**7)

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    B = [a for a in A if a != X]
    print(*B, sep=" ")


if __name__ == '__main__':
    main()