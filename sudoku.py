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
def forwardcheck(assignment:list,domain:list,size:int) -> bool:
    csp = CSP(assignment,domain,size)
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

if __name__ == "__main__":
    domain = [1,2,3]
    assignment = [  1,0,2,
                    0,0,1,
                    0,2,0]
    size = 3
    csp = CSP(domain,assignment,size)

    print(csp.consistent())
    print(csp.complete())

    vars = csp.vars
    for i in range(size*size):
        dom = getDomain(csp,csp.vars[i])
        var = csp.vars[i]
        if var.value == 0:
            print(dom,end=" ")
        else:
            print(var.value,end=" ")
        if i%size == size-1:
            print("")

    print(select_unassigned_variable(csp)) 






    