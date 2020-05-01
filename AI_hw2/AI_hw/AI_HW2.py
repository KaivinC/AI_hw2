import time as t
import nor
import FW
import D
import M
import M_D
import D_L
import M_L
import M_D_L
import gernerator
import matplotlib.pyplot as plt
boardLength = 15
boardWidth = 15

def CheckValid(board,Index,goal):
    flag = 0
    # upper left
    if(goal-Index==-(boardWidth-1) and goal%boardWidth!=0):
        flag=1
    # upper
    elif(goal-Index==-(boardWidth) ):
        flag=1
    # upper right
    elif(goal-Index==-(boardWidth+1) and (goal+1)%boardWidth!=0):
        flag=1
    # right
    elif(goal-Index ==-1 and (goal+1)%boardWidth!=0 ):  
        flag=1
    # left
    elif(goal-Index ==1 and goal%boardWidth!=0 ):  
        flag=1
    # bottom left
    elif(goal-Index==(boardWidth-1) and (goal+1)%boardWidth!=0):
        flag=1
    # bottom
    elif(goal-Index==(boardWidth) ):
        flag=1
    # bottom right
    elif(goal-Index==(boardWidth+1) and (goal)%boardWidth!=0):
        flag=1
    if(flag):
        return True
    else:
        False

def main():
    #board = [-1, -1, -1, 1, 1, -1, -1, 3, -1, -1, -1, 0, 2, 3, -1, 3, 3, 2, -1, -1, 2, -1, -1, -1, -1, 2, 2, 3, -1, 3, -1, 1, -1, -1, -1, 1]
    #board = [-1, -1, -1, 1, 1, 1, 3, 4, -1, 2, -1, -1, 2, -1, -1, -1, -1, -1, -1, -1, 2, 2, -1, 2, 1, 2, -1, -1, 1, -1, -1, 1, -1, 1, 0, -1]
    #board = [-1, -1, -1, -1, -1, -1, -1, 2, 2, 2, 3, -1, -1, 2, 0, 0, 2, -1, -1, 2, 0, 0, 2, -1, -1, 3, 2, 2, 2, -1, -1, -1, -1, -1, -1, -1]
    #board = [-1, 1, -1, 1, 1, -1, 2, 2, 3, -1, -1, 1, -1, -1, 5, -1, 5, -1, 2, -1, 5, -1, -1, -1, -1, 2, -1, -1, 3, -1, -1, -1, 1, 1, -1, 0]
    expandNum_nor=[]
    expandNum_FW=[]
    expandNum_M=[]
    expandNum_D=[]
    expandNum_M_L=[]
    expandNum_D_L=[]
    expandNum_M_D=[]
    expandNum_M_D_L=[]

    nor_time=[]
    FW_time=[]
    M_time=[]
    D_time=[]
    M_L_time=[]
    D_L_time=[]
    M_D_time=[]
    M_D_L_time=[]
    BoardSize=[i for i in range(6,10)]
    for x in range(6,10):
        global boardLength
        global boardWidth
        boardLength=x
        boardWidth=x

        hintNum=round((x*x*4)/9)
        mineNum=round((x*x*5)/18)
        ALLED=[0,0,0,0,0,0,0,0]
        ALLTIME=[0,0,0,0,0,0,0,0]

        for y in range(500):
            boar=gernerator.make_question((x,x),mineNum,hintNum)
            board=[]
            for i in range(boardLength):
                for j in range(boardWidth):
                    board.append(boar[0][i][j])


            linkHint=[[] for i in range (boardLength*boardWidth)]
            hintMap={}

            for i in range (boardLength*boardWidth):
                for j in range(boardLength*boardWidth):
                    if (board[j]> -1 and CheckValid(board,j,i)):
                        linkHint[i].append(j)


            for i in range(boardLength*boardWidth):
                for j in range (len(linkHint[i])):
                    if linkHint[i][j] not in hintMap:
                        hintMap[linkHint[i][j]] = list()
                    if(board[i]<0):
                        hintMap[linkHint[i][j]].append(i)



            copyBoard=board[:]
            t_begin_nor=t.time()
            ALLED[0]+=nor.nor(copyBoard,linkHint,boardLength,boardWidth)
            t_end_nor=t.time()
            ALLED[0]+=(t_end_nor-t_begin_nor)

            copyBoard=board[:]
            t_begin_FW=t.time()
            ALLED[1]+=FW.FW(copyBoard,linkHint,hintMap,boardLength,boardWidth)
            t_end_FW=t.time()
            ALLTIME[1]+=(t_end_FW-t_begin_FW)

            # copyBoard=board[:]
            # t_begin_M=t.time()
            # ALLED[2]+=M.M(copyBoard,linkHint,hintMap,boardLength,boardWidth)
            # t_end_M=t.time()
            # ALLTIME[2]+=(t_end_M-t_begin_M)

            # copyBoard=board[:]
            # t_begin_D=t.time()
            # ALLED[3]+=D.D(copyBoard,linkHint,hintMap,boardLength,boardWidth)
            # t_end_D=t.time()
            # ALLTIME[3]+=(t_end_D-t_begin_D)

            # copyBoard=board[:]
            # t_begin_M_L=t.time()
            # ALLED[4]+=M_L.M_L(copyBoard,linkHint,hintMap,boardLength,boardWidth)
            # t_end_M_L=t.time()
            # ALLTIME[4]+=(t_end_M_L-t_begin_M_L)

            # copyBoard=board[:]
            # t_begin_D_L=t.time()
            # ALLED[5]+=D_L.D_L(copyBoard,linkHint,hintMap,boardLength,boardWidth)
            # t_end_D_L=t.time()
            # ALLTIME[5]+=(t_end_D_L-t_begin_D_L)

            # copyBoard=board[:]
            # t_begin_M_D=t.time()
            # ALLED[6]+=M_D.M_D(copyBoard,linkHint,hintMap,boardLength,boardWidth)
            # t_end_M_D=t.time()
            # ALLTIME[6]+=(t_end_M_D-t_begin_M_D)

            # copyBoard=board[:]
            # t_begin_M_D_L=t.time()
            # ALLED[7]+=M_D_L.M_D_L(copyBoard,linkHint,hintMap,boardLength,boardWidth)
            # t_end_M_D_L=t.time()
            # ALLED[7]+=(t_end_M_D_L-t_begin_M_D_L)
        
        expandNum_nor.append(ALLED[0]/500)
        expandNum_FW.append(ALLED[1]/500)
        expandNum_M.append(ALLED[2]/500)
        expandNum_D.append(ALLED[3]/500)
        expandNum_M_L.append(ALLED[4]/500)
        expandNum_D_L.append(ALLED[5]/500)
        expandNum_M_D.append(ALLED[6]/500)
        expandNum_M_D_L.append(ALLED[7]/500)

        nor_time.append(ALLTIME[0]/500)
        FW_time.append(ALLTIME[1]/500)
        M_time.append(ALLTIME[2]/500)
        D_time.append(ALLTIME[3]/500)
        M_L_time.append(ALLTIME[4]/500)
        D_L_time.append(ALLTIME[5]/500)
        M_D_time.append(ALLTIME[6]/500)
        M_D_L_time.append(ALLTIME[7]/500)

    plt.plot(BoardSize, expandNum_nor, label='Backtricking', color='red')
    plt.plot(BoardSize, expandNum_FW, label='Forward Check', color='blue')
    # plt.plot(BoardSize, expandNum_M, label='MRV', color='purple')
    # plt.plot(BoardSize,expandNum_D,label='Degree',color='yellow')
    # plt.plot(BoardSize,expandNum_M_L,label='MRV+LCV',color='green')
    # plt.plot(BoardSize,expandNum_D_L,label='Degree+LCV',color='brown')
    # plt.plot(BoardSize,expandNum_M_D,label='MRV+Degree',color='black')
    # plt.plot(BoardSize,expandNum_M_D_L,label='MRV+Degree+LCV',color='pink')
    plt.xlabel('Board size')
    plt.ylabel('EXPANDED NODE')
    plt.title('SPACE:B vs FW')
    plt.legend(loc='best')
    plt.show()
    plt.close()


    plt.plot(BoardSize, nor_time, label='Backtricking', color='red')
    plt.plot(BoardSize, FW_time, label='Forward Check', color='blue')
    #plt.plot(BoardSize, M_time, label='MRV', color='purple')
    #plt.plot(BoardSize,D_time,label='Degree',color='yellow')
    #plt.plot(BoardSize,M_L_time,label='MRV+LCV',color='green')
    #plt.plot(BoardSize,D_L_time,label='Degree+LCV',color='brown')
    #plt.plot(BoardSize,M_D_time,label='MRV+Degree',color='black')
    #plt.plot(BoardSize,M_D_L_time,label='MRV+Degree+LCV',color='pink')
    plt.xlabel('Board size')
    plt.ylabel('Using time')
    plt.title('TIME:B vs FW')
    plt.legend(loc='best')
    plt.show()

if __name__ == "__main__":
        main()
