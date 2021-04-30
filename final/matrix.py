
def matrix(board): 
    # your code goes here:
    ans = float("inf")
    m = len(board[0])
    n = len(board)
    for i in range(m):
        ans = min(ans, board[0][i])
    for i in range(1, n):
        ans = float("inf")
        for j in range(m):
            if(j > 0 and j < (m-1)):
                board[i][j] += min(board[i - 1][j], min(board[i - 1][j - 1], board[i - 1][j + 1])) 
            elif(j > 0):
               board[i][j] += min(board[i - 1][j], board[i - 1][j - 1])
            elif (j < m - 1): 
                board[i][j] += min(board[i - 1][j], board[i - 1][j + 1]) 
            
            ans = min(board[i][j], ans)
    #print(ans)
    return ans




if __name__ == "__main__":
    board = [[1,2,3],[4,5,6],[7,0,2]]
    board2 = [[1]]
    board3 = [[1,2,3]]
    board4 = [[1,2,3,0],[4,5,1,6],[7,0,2,0]]
    print(matrix(board))
    print(matrix(board2))
    print(matrix(board3))
    print(matrix(board4))

