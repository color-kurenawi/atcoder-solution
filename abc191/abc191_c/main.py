#!/usr/bin/env python3

import sys
sys.setrecursionlimit(10**7)

def main():
    H, W = map(int, input().split())
    field = [input() for _ in range(H)]
    
    first_y, first_x = -1, -1
    for i in range(H):
        for j in range(W):
            if field[i][j] == "#":
                first_y, first_x = (i, j)
                break
        if first_y != -1:
            break
    ans = 1
    y, x = first_y, first_x
    state = "top"
    while True:
        # print(state, x, y)
        if state == "top":
            if field[y-1][x] == "#":
                y -= 1
                state = "left"
                ans += 1
            elif field[y][x] == "#":
                x += 1
            else:
                y += 1
                state = "right"
                ans += 1
                
        elif state == "right":
            if field[y][x] == "#":
                x += 1
                state = "top"
                ans += 1
            elif field[y][x-1] == "#":
                y += 1
            else:
                x -= 1
                state = "bottom"
                ans += 1
                
        elif state == "bottom":
            if field[y][x-1] == "#":
                y += 1
                state = "right"
                ans += 1
            elif field[y-1][x-1] == "#":
                x -= 1
            else:
                y -= 1
                state = "left"
                ans += 1
        
        elif state == "left":
            if field[y-1][x-1] == "#":
                x -= 1
                state = "bottom"
                ans += 1
            elif field[y-1][x] == "#":
                y -= 1
            else:
                x += 1
                state = "top"
                ans += 1
        
        if x == first_x and y == first_y:
            break
    
    print(ans)


if __name__ == '__main__':
    main()