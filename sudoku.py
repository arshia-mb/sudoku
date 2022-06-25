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

if __name__ == "__main__":
    domain = [1,2,3]
    assignment = [  1,2,3,
                    2,3,1,
                    3,1,2]
    size = 3
    csp = CSP(domain,assignment,size)

    print(csp.consistent())
    print(csp.complete())

    vars = csp.vars
    for i in range(size*size):
        print(getDomain(csp,csp.vars[i]),end=" ")
        if i%size == size-1:
            print("") 






    