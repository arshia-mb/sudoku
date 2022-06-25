#Solving sudoku by using CSP
#Arshia Moradi 21 June 2022

from csp import CSP
from csp import Variabel

#Finds the avialbe values for a variable - Domain
def getDomain(csp:CSP,var:Variabel) -> list:
    all_domain = csp.domain
    variabels = csp.vars
    if var.value != 0:
        return [var.value]
    domain = all_domain.copy() #All the values that can be assigned
    #Check which ones are viabel
    for index in var.friends:
        if variabels[index].value in domain:
            domain.remove(variabels[index].value)
    return domain

#Checks the assignment of the values is okay or not
def forwardcheck(csp:CSP) -> bool:
    for i in range(size*size):
        domain = getDomain(csp,csp.vars[i])
        if len(domain) == 0:
            return False
    return True


#MRV hurestic to chose what value to be assigned
def select_unassigned_variable(csp:CSP) -> int:
    size = csp.size
    min_val = size+1 #max value cannot be more than domain size
    max_con = -1 #the degree to that variabel constrains others
    index = size*size #The variabel that is chosen
    for i in range(size*size):
        variabel =  csp.vars[i]
        if variabel.value == 0 : #Check if it's assigned or not
            dsize = getDomain(csp,csp.vars[i]) #size of the domain of unassigned
            #Check if degree hurestic is needed
            if len(dsize) == min_val:
                con = check_conflicts(csp,variabel)
                if con > max_con:
                    index = i
                    max_con = con 
            #Check if the values domain is smaller
            if len(dsize) < min_val:
                index = i
                min_val = len(dsize) 
                max_con = check_conflicts(csp,variabel)
    return index   

#Check how many variabels that are connect to var are not assigned a value
def check_conflicts(csp:CSP,var:Variabel) -> int:
    conflicts = 0 #Number of 
    for variabels in var.friends:
        var = csp.vars[variabels]
        if var.value == 0:
            conflicts = conflicts + 1
    return conflicts

#Back tracking search algorithm
def recurseive_backtracing(csp:CSP): #returns soloution or failure
    if csp.complete(): #return answer
        return csp
    var_index = select_unassigned_variable(csp) #Find the next variable to be assigned
    var = csp.vars[var_index]
    for value in getDomain(csp,var): #Iterate on the domain
        csp.vars[var_index].value = value #Change the assignment
        if csp.consistent(): #If compelete then do recursive search
            resault = recurseive_backtracing(csp)
            if resault != False: #if answer is found then return the assignment
                return resault
        csp.vars[var_index].value = 0 #if the answer is not consistent or not found then remake the assignment
    return False   

if __name__ == "__main__":
    assignment = [  3,0,6,5,0,8,4,0,0,
                    5,2,0,0,0,0,0,0,0,
                    0,8,7,0,0,0,0,3,1,
                    0,0,3,0,1,0,0,8,0,
                    9,0,0,8,6,3,0,0,5,
                    0,5,0,0,9,0,6,0,0,
                    1,3,0,0,0,0,2,5,0,
                    0,0,0,0,0,0,0,7,4,
                    0,0,5,2,0,6,3,0,0]
    size = 9
    domain = [i for i in range(1,size+1)] 
    csp = CSP(domain,assignment,size)
    answer = recurseive_backtracing(csp)
    if answer == False:
        print("No answer found!")
    else:
        for i in range(size*size):
            print(answer.vars[i].value,end=" ")
            if i%size == size-1:
                print("")





    