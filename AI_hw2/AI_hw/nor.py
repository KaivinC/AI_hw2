
def FinalCheck(copyBoard,state,path):
    for i in copyBoard:
        if(i>0):
            return False
    return True

def Restore(copyBoard,state,path,hintLink):
    now=path.pop()
    state[now]=2
    for i in hintLink[now]:
        copyBoard[i]+=1

def nor(copyBoard,hintLink,boardLength,boardWidth):
    state = [2 for i in range(boardLength*boardWidth)]
    path=[]
    stack=[]
    

    expandNum=0
    for i,val in enumerate(copyBoard):
        if val>-1:
            state[i]=3
    first_point=0
    for i in range (boardLength*boardWidth):
        if(state[i]!=3):
            first_point=i
            break
    stack.append((first_point,0))
    stack.append((first_point,1))
    while(stack):
        expandNum+=1
        now=stack.pop()
        if(state[now[0]]!=3):
            flag=1
            if(now[1]):      
                for i,val in enumerate(hintLink[now[0]]):
                    if(copyBoard[val]-1>=0):
                        copyBoard[val]-=1
                    else:
                        for j in range(0,i):
                            copyBoard[hintLink[now[0]][j]]+=1
                        flag=0
                        break

            if(flag and now[0]<boardLength*boardWidth):
                for i in range (len(path)): # restore
                    if(path[i]==now[0]):
                        while(i+1!=len(path)):
                            state[path[len(path)-1]]=2
                            path.pop()
                        Restore(copyBoard,state,path,hintLink)
                        break

                state[now[0]]=now[1]
                path.append(now[0])
                tmp=now[0]+1
                while(tmp < boardLength*boardWidth and state[tmp]==3 ):
                    tmp+=1

                if(tmp==boardLength*boardWidth):
                    if(FinalCheck(copyBoard,state,path)):
                        break
                    else:
                        continue

                stack.append((tmp,0))
                stack.append((tmp,1))

    # for i in range(boardLength):
    #     for j in range(boardWidth):
    #         print(state[i*boardWidth+j],end=" ")
    #     print("\n")
    
    return expandNum