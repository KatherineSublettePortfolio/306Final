
def triangle(board): 
    # your code goes here:
    ans = float("inf")
    #m = len(board[0])
    #n = len(board)
    for i in range(len(board)-2, -1, -1):
        for j in range(len(board[i])-1, -1, -1):
            board[i][j] += min(board[i+1][j], board[i+1][j+1])
    return board[0][0]
    


if __name__ == "__main__":
    board = [[2],[5,4],[1,4,7],[8,6,9,6]]
    board2 = [[1]]
    board3 = [[1],[2,3],[7,5,9]]
    print(triangle(board))
    print(triangle(board2))
    print(triangle(board3))


