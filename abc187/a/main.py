#!/usr/bin/env python3


def main():
    a, b = input().split()
    a_sum = sum(int(digit) for digit in a)
    b_sum = sum(int(digit) for digit in b)
    if a_sum >= b_sum:
        print(a_sum)
    else:
        print(b_sum) 

if __name__ == '__main__':
    main()