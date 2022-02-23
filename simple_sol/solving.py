from random import *
def get_randomly_solutions(items, knapsack):
    s=[]
    ss=[]        #single solution
    su=0
    for r in range(10):
        for i in range(len(items)):
            for j in range(len(items)):
                su+=1
                ss.append(randint(0, 1))
            if(verify(items, ss, knapsack)[0]):
                s.append([ss, verify(items, ss, knapsack)[1]])
            ss=[]
    for i in range(len(s)):
        print('The ', i, 'th solution=', s[i][0], 'And its profit=', s[i][1])
    max_profit=s[0]
    for i in range(1, len(s)):
        if(s[i][1]>=max_profit[1]):max_profit=s[i]
    print('The optimal solution=', max_profit[0],' And its profit=', max_profit[1])
    print('sum=', su)
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