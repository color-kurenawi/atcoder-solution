#!/usr/bin/env python3


def main():
    N = int(input())
    xys = [list(map(int, input().split())) for _ in range(N)]
        
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            x1, y1 = xys[i]
            x2, y2 = xys[j]
            
            if x1 > x2:
                tmp = (x1, y1)
                x1, y1 = (x2, y2)
                x2, y2 = tmp
                
            dx = x2 - x1
            dy = y2 - y1
            
            if -dx <= dy and dy <= dx:
                count += 1
                
    print(count)

if __name__ == '__main__':
    main()