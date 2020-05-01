def Initailize_mineBound(mineBound, Index, mineMap, board):
    # upper left
    if(Index-(boardWidth+1) >= 0 and mineMap[Index-(boardWidth+1)]):
        mineBound[Index-(boardWidth+1)] = max(mineBound[Index -
                                                        (boardWidth+1)], board[Index-(boardWidth+1)])
    # upper
    if(Index-(boardWidth) >= 0 and mineMap[Index-(boardWidth)]):  
        mineBound[Index-(boardWidth)] = max(mineBound[Index -
                                                        (boardWidth)], board[Index-(boardWidth)])
    # upper right
    if(Index-(boardWidth-1) >= 0 and mineMap[Index-(boardWidth-1)]):
        mineBound[Index-(boardWidth-1)] = max(mineBound[Index -
                                                        (boardWidth-1)], board[Index-(boardWidth-1)])
    # right
    if(Index-1 >= 0 and mineMap[Index-1]):  
        mineBound[Index-1] = max(mineBound[Index-1], board[Index-1])
    # left
    if(Index+1 < boardLength*boardWidth and mineMap[Index+1]):  
        mineBound[Index+1] = max(mineBound[Index+1], board[Index+1])
    # bottom left
    if(Index+(boardWidth-1) < boardLength*boardWidth and mineMap[Index+(boardWidth-1)]):
        mineBound[Index+(boardWidth-1)] = max(mineBound[Index +
                                                        (boardWidth-1)], board[Index+(boardWidth-1)])
    # bottom
    if(Index+(boardWidth) < boardLength*boardWidth and mineMap[Index+(boardWidth)]):  
        mineBound[Index+(boardWidth)] = max(mineBound[Index +
                                                        (boardWidth)], board[Index+(boardWidth)])
    # bottom right
    if(Index+(boardWidth+1) < boardLength*boardWidth and mineMap[Index+(boardWidth+1)]):
        mineBound[Index+(boardWidth+1)] = max(mineBound[Index +
                                                        (boardWidth+1)], board[Index+(boardWidth+1)])


