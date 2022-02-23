from random import *
def solve(items, knapsack):
    solutions=[]
    sol=[]
    for i in range(10):
        for i in range(len( items)):
            sol.append(randint(0, 1))
        if(verify(items, knapsack, sol)[0]):
            solutions.append((sol, verify(items, knapsack, sol)[1]))
        sol=[]
    for i in range(len(solutions)):
        print(solutions[i])
    #select a solution randomly
    sr=randint(0, len(solutions))

def neighberhood(sol):
    ran_in=randint(0, len(sol))
    if(sol[ran_in]==1):
        sol[ran_in]==0
    else:
        sol[ran_in]==1
def verify(items, knapsack, sol):
    s1=0;s2=0;profit=0
    for i in range(len(items)):
        s1=s1+sol[i]*items[i].resource[0]
        s2=s2+sol[i]*items[i].resource[1]
        profit=profit+sol[i]*items[i].profit
    if(s1<=knapsack.capacities[0])and (s2<=knapsack.capacities[1]):
        return True, profit
    else:
        return False, profit