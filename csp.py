#CSP class that is used in sudoku solver
#Arshia Moradi 23 June 2022

class Variabel:
    def __init__(self,value:int,friends:list):
        self.value = value
        self.friends = friends
emtyVar = Variabel(0,[])

class CSP:
    #initialize csp
    def __init__(self,domain:list,assignment:list,size:int)-> None:
        self.domain = domain
        self.size = size
        self.vars = [emtyVar for i in range(size*size)] 
        #Creating the variabel list
        for i in range(size*size):
            value = assignment[i]
            friends = self.getNeighbors(i) 
            self.vars[i] = Variabel(value,friends)

    #finding the nighbor list for each variable
    def getNeighbors(self,index:int) -> list:
        grid = self.size #The grid size of the puzzle
        friends = []
        i = int((index/grid))*grid #getting the start of the row
        j = index%grid #getting the colummn
        #Adding the row
        for x in range(i,i+grid):
            if x != index:
                friends.append(x)
        for x in range(grid):
            if j != index:
                friends.append(j)
            j = j + grid
        #Adding the column
        return friends

    #checks the consistency of the assignments
    def consistent(self) -> bool:
        size = self.size
        rowConsistent = [[False for i in range(size+1)] for j in range(size)] #Each row domain consistency
        colConsistent = [[False for i in range(size+1)] for j in range(size)] #Each column domain consistency
        for i in range(size*size):
            row = int(i/size)
            column = i%size
            val = self.vars[i].value
            #Check consistency of the row
            if val != 0 and rowConsistent[row][val]:
                return False
            rowConsistent[row][val] = True 
            #Check consistency of the column
            if val != 0 and colConsistent[column][val]:
                return False
            colConsistent[column][val] = True 
        return True

    #Checks if the assignment is compelte
    def complete(self) -> bool:
        #First it has to be consistent
        if not self.consistent():
            return False

        #now every variable must be assigned
        for i in range(self.size*self.size):
            if self.vars[i].value == 0: #if there is 0 then it's not assigned
                return False
        return True
        

