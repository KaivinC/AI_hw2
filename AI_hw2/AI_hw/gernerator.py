import random
import time
# It makes me easier to get neighbors

neighbor = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
            (0, 1), (1, -1), (1, 0), (1, 1)]
def Neighbor(BoardSize, x, y):
    '''
    To get the list of neighbor
    '''
    Neighbor_List = []
    for (dx, dy) in neighbor:
        if (x + dx < 0 or x + dx >= BoardSize[0] or
                y + dy < 0 or y + dy >= BoardSize[1]):
            continue
        Neighbor_List.append((x+dx, y+dy))
    return Neighbor_List

def make_question(BoardSize, num_mines, num_Hint):
    ans = [[None for j in range(BoardSize[1])]for i in range(BoardSize[0])]
    for _ in range(num_mines):
        i = random.randint(0, BoardSize[0]-1)
        j = random.randint(0, BoardSize[1]-1)
        while ans[i][j] is not None:
            i = random.randint(0, BoardSize[0]-1)
            j = random.randint(0, BoardSize[1]-1)
        ans[i][j] = 'X'
        N = Neighbor(BoardSize, i, j)
        random.shuffle(N)
        for (Nx, Ny) in N:
            if ans[Nx][Ny] is None:
                ans[Nx][Ny] = 'Hint'
                num_Hint -= 1
                break
            if ans[Nx][Ny] == 'Hint':
                break
    for i in range(BoardSize[0]):
        for j in range(BoardSize[1]):
            if ans[i][j] is None:
                BREAK = False
                for (Nx, Ny) in Neighbor(BoardSize, i, j):
                    if ans[Nx][Ny] is not None:
                        BREAK = True
                        break
                if BREAK:
                    continue
                ans[i][j] = 'Hint'
                num_Hint -= 1
    for _ in range(num_Hint):
        i = random.randint(0, BoardSize[0]-1)
        j = random.randint(0, BoardSize[1]-1)
        while ans[i][j] is not None:
            i = random.randint(0, BoardSize[0]-1)
            j = random.randint(0, BoardSize[1]-1)
        ans[i][j] = 'Hint'
    for i in range(BoardSize[0]):
        for j in range(BoardSize[1]):
            if ans[i][j] == 'Hint':
                ans[i][j] = 0
                for (Nx, Ny) in Neighbor(BoardSize, i, j):
                    if ans[Nx][Ny] == 'X':
                        ans[i][j] += 1
    Q = [[None for j in range(BoardSize[1])]for i in range(BoardSize[0])]
    for i in range(BoardSize[0]):
        for j in range(BoardSize[1]):
            if type(ans[i][j]) == int:
                Q[i][j] = ans[i][j]
            else:
                Q[i][j] = -1
    return Q, ans
    
def check(BoardSize, num_mines, MAP):
    CountTotal = 0
    for i in range(BoardSize[0]):
        for j in range(BoardSize[1]):
            if MAP[i][j] == 'X':
                CountTotal += 1
            if type(MAP[i][j]) == int:
                Count = 0
                for (Nx, Ny) in Neighbor(BoardSize, i, j):
                    if MAP[Nx][Ny] == 'X':
                        Count += 1
                if Count != MAP[i][j]:
                    return False
    if CountTotal == num_mines:
        return True
    else:
        return False