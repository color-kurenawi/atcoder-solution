#!/usr/bin/env python3

def main():
    N = int(input())
    Ss = [input() for _ in range(N)]

    d = set()
    for S in Ss:
        if S[0] == "!" and S[1:] in d:
            print(S[1:])
            exit()
        elif S[0] != "!" and "!" + S in d:
            print(S)
            exit()            
        else:
            d.add(S)
            
    print("satisfiable")
    
if __name__ == '__main__':
    main()