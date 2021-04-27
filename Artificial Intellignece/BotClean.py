#!/usr/bin/python

# Head ends here

def next_move(r, c, board):
    md=99999
    nearest=None
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]=='d':
                d=abs(r-i)+abs(c-j)
                if d<md:
                    md=d
                    nearest=i,j
                
    i,j=nearest
    if (i,j)==(r,c):
        print('CLEAN')
    elif r<i:
        print( 'DOWN')
    elif c<j:
        print( 'RIGHT')
    elif r>i:
        print( 'UP')
    elif c>j:
        print( 'LEFT')
    
            
    

# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)