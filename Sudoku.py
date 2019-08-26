# import only system from os 
from os import system, name 
# import sleep to show output for some time period 
from time import sleep 




# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

#Find Cell with no value
def findEmptyCell(grid):
    for x in range(0,len(grid)):
        
        for y in range(0,len(grid)):
            if(grid[x][y]==0):
                return x,y
    return True
#check if the value is present in any other cells Horizontallly
def checkHorizontal(guessNum,y,grid):
    for searchX in range(len(grid)):
                gX=grid[searchX][y]
                if(gX==guessNum):
                    return False
    return True

#check if the value is present in any other cells Vertically
def checkVertical(guessNum,x,grid):
    for searchY in range(0,len(grid)):
            gY=grid[x][searchY]
            if(gY==guessNum):
                 return False
            else:
                continue
    return True


     
def isSolved(grid):
    for k in range(len(grid)):
        if all(grid[k]):
            continue
        else:
            return False
    return True

def printBoard(grid):
    #print(grid, end="", flush=True)
        print("===========================================")
        for j in grid:
            print(j)
        #sleep(1)
        print("===========================================")
        clear()
#Main
def sudokuSolver(grid):
        if isSolved(grid):
            wait(5)
            input("done")
        #input values
        if(not findEmptyCell(grid)):
            return True
        x,y=findEmptyCell(grid)
        
        #grid[eX][eY]=val
        #try to guess value by checking if the number exists horizontally or vertically

        for guessNum in range(1,len(grid)+1):
                if(checkHorizontal(guessNum,y,grid) and checkVertical(guessNum,x,grid)):
                    grid[x][y]=guessNum
                    printBoard(grid)
                    if(sudokuSolver(grid)):
                        for j in grid:
                            print(j)
                        return True
                    backtrack=+1
                    #print('backtrack:',backtrack)
                    grid[x][y]=0
        return False
        
       
##board=[[5,1,7,6,0,0,0,3,4],
##	[2,8,9,0,0,4,0,0,0],
##	[3,4,6,2,0,5,0,9,0],
##	[6,0,2,0,0,0,0,1,0],
##	[0,3,8,0,0,6,0,4,7],
##	[0,0,0,0,0,0,0,0,0],
##	[0,9,0,0,0,0,0,7,8],
##	[7,0,3,4,0,0,5,6,0],
##	[0,0,0,0,0,0,0,0,0]]
board=[[3,0,6,5,0,8,4,0,0], 
          [5,2,0,0,0,0,0,0,0], 
          [0,8,7,0,0,0,0,3,1], 
          [0,0,3,0,1,0,0,8,0], 
          [9,0,0,8,6,3,0,0,5], 
          [0,5,0,0,9,0,6,0,0], 
          [1,3,0,0,0,0,2,5,0], 
          [0,0,0,0,0,0,0,7,4], 
          [0,0,5,2,0,6,3,0,0]]
print("===============================================")
#printBoard(board)
sudokuSolver(board)

