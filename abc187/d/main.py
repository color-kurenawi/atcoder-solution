#!/usr/bin/env python3

def main():
    N = int(input())
    
    A = [0]*N
    B = [0]*N
    diff = [0]*N
    for i in range(N):
        a, b = map(int, input().split())
        A[i] = a
        B[i] = b
        diff[i] = 2*a + b

    need = sum(A)
    diff.sort(reverse=True)
    
    ans = 0
    score = 0
    if score > need:
        print(ans)
        exit()
    for d in diff:
        score += d
        ans += 1
        if score > need:
            print(ans)
            exit()

if __name__ == '__main__':
    main()