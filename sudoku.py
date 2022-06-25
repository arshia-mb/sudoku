#Solving sudoku by using CSP
#Arshia Moradi 21 June 2022

from csp import CSP
from csp import Variabel



if __name__ == "__main__":
    domain = [1,2,3]
    assignment = [  1,2,3,
                    2,3,1,
                    3,1,2]
    size = 3
    csp = CSP(domain,assignment,size)

    print(csp.consistent())
    print(csp.complete())


    