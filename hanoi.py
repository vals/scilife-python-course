"""Solve 'Towers of Hanoi'
"""
import sys

PRINT = False

@profile
def solve(g,n):
    X = [sum(g[0])]
    Y = [sum(g[1])]
    Z = [sum(g[2])]

    moved = 0
    for i in range(2**n - 1):
        tops = [a[0] for a in g]
        movable = False
        j = 0
        while not movable:
            max_legal = max([t for t in tops if g[j][0] % 2 != t % 2])
            if g[j][0] != moved and g[j][0] > 0:
                num_zeros = len([z for z in tops if z == 0])
                if g[j][0] < max_legal or num_zeros > 0:
                    movable = True
            if not movable:
                j += 1
        
        moved = g[j][0]
        
        legal = False
        k = 2
        while not legal:
            if (tops[k] % 2 != g[j][0] % 2 and g[j][0] < tops[k]) or tops[k] == 0:
                legal = True
            if not legal:
                k -= 1
        
        g[k] = [g[j][0]] + g[k]
        g[j] = g[j][1::]

        if PRINT:
            print g

        S = [sum(s) for s in g]
        X += [S[0]]
        Y += [S[1]]
        Z += [S[2]]
    
    return (X,Y,Z)


if __name__ == "__main__":
    n = int(sys.argv[-1])
    game = [range(1,n+1)+[0], [0], [0]]

    X, Y, Z = solve(game,n)
