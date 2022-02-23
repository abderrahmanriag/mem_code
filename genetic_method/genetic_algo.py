from random import *
def get_randomly_solutions(items, knapsack):
    s=[]
    ss=[]        #single solution
    for r in range(3):
        for i in range(len(items)):
            for j in range(len(items)):
                ss.append(randint(0, 1))
            if(verify(items, ss, knapsack)[0]):
                s.append([ss, verify(items, ss, knapsack)[1]])
            ss=[]
    print('All constraints are verified')
    for i in range(len(s)):
        print(s[i])
def verify(items, ss, knapsack):
    s1=0;s2=0;profit=0
    for i in range(len(items)):
            s1=s1+ss[i]*items[i].resource[0]
            s2=s2+ss[i]*items[i].resource[1]
            profit=profit+ss[i]*items[i].profit
    if(s1<=knapsack.capacities[0] and s2<=knapsack.capacities[1]):
        return True, profit
    else:
        return False, profit