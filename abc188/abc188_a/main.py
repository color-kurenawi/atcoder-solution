#!/usr/bin/env python3

import sys
sys.setrecursionlimit(10**7)

def main():
    X, Y = map(int, input().split())
    
    if X + 3 > Y and Y + 3 > X:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()