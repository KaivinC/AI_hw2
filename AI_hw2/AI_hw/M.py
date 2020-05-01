
def FinalCheck(board,state,linkHint,boardLebgth,boardWidth):
    copyboard=board[:]
    flag=1
    for i in range(boardLebgth*boardWidth):
        if(state[i]==1):
            for j in linkHint[i]:
                copyboard[j]-=1
                if(copyboard[j]<0):
                    flag=0
    if(flag):
        return True
    else:
        return False

def M(copyBoard,linkHint,hintMap,boardLength,boardWidth):
    path=[]
    stack=[]
    unassign=[-1]
    expandNum=0
    state = [2 for i in range(boardLength*boardWidth)]
    mineBound={}

    for i,val in enumerate(copyBoard):
        if val>-1:
            state[i]=3
        else:
            unassign.append(i)
        first_point=0

    for i in range (boardLength*boardWidth):
        if(state[i]!=3):
            first_point=i
            break
    stack.append((first_point,0))
    stack.append((first_point,1))

    for i in range(boardLength*boardWidth):
        for j in range(len(linkHint[i])):
            if(linkHint[i][j] not in mineBound):
                mineBound[linkHint[i][j]]=(0,len(hintMap[linkHint[i][j]]))

    while(stack):
        expandNum+=1
        now=stack.pop()
        push_or_not=1

        if(state[now[0]]!=3):
            for i in range(len(path)):
                if(path[i]==now[0]):
                    while(path[len(path)-1]!=now[0]):
                        t=path.pop()
                        state[t]=2
                        unassign.append(t)
                    t=path.pop()
                    state[t]=2
                    unassign.append(t)
                    break
            
            
            state[now[0]]=now[1]
            candidate=now
            for val in linkHint[now[0]]:
                lower=0
                upper=0
                for pos in hintMap[val]:
                    lower += 0 if(state[pos]==2) else state[pos]
                    upper += 1 if(state[pos]>0) else 0
                if(lower==copyBoard[val]):
                    for pos in hintMap[val]:
                        if(state[pos]==2):
                            candidate=(pos,0)
                            break
                elif(upper==copyBoard[val]):
                    for pos in hintMap[val]:
                        if(state[pos]==2):
                            candidate=(pos,1)
                            break
                if(lower>copyBoard[val] or upper<copyBoard[val]):
                    state[now[0]]=2
                    push_or_not=0
                    break

            if(push_or_not):
                path.append(now[0])
                unassign.remove(now[0])
                tmp=unassign[len(unassign)-1]

                if(len(unassign)==1):
                    if(FinalCheck(copyBoard,state,linkHint,boardLength,boardWidth)):
                        break
                    else:
                        continue

                if(tmp!=-1):
                    if(state[tmp]>state[candidate[0]]):
                        stack.append((tmp,0))
                        stack.append((tmp,1))
                    else:
                        stack.append(candidate)
                        

    # for i in range(boardLength):
    #     for j in range(boardWidth):
    #         if(state[i*boardWidth+j]<=1):
    #             print(state[i*boardWidth+j],end="  ")
    #         else:
    #             print("*%d"%(copyBoard[i*boardWidth+j]),end=" ")
    #     print("\n")

    # for i in range(boardLength):
    #     for j in range(boardWidth):
    #         print(state[i*boardWidth+j],end=" ")
    #     print("\n")
    
    return expandNum