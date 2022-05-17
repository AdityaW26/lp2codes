global N
N = 4

def printNQ(board):
    for i in range(len(board)):
        print(board[i])

def isSafe(board,row,col):

    #left row
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j] == 1:
            return False

    for i,j in zip(range(row,N,-1),range(col,-1,-1)):
        if board[i][j] == 1:
            return False

    return True

def solveNQ(board,col):

    if col>=N :
        return True

    for i in range(N):
        if isSafe(board,i,col):

            board[i][col] = 1

            if solveNQ(board,col+1)==True :
                return True

            board[i][col] = 0

    return False

def solve():

    board = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ]

    if solveNQ(board,0)==False:
        print("NO SOLUTION")
        return False

    printNQ(board)
    return True

solve()