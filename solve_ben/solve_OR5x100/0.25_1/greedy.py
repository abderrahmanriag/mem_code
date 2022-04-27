import ConvToList as ctl
from knapsack import *
from object import *
import verify as vr
import random
import efficiency as eff
import info
import pickle

def BestAndWorst(solutions):
                    b=solutions[0]
                    w=solutions[0]
                    for i in range(len(solutions)):
                                        if solutions[i][1]>=b[1]:
                                                            b=solutions[i]
                                        if solutions[i][1]<=w[1]:
                                                            w=solutions[i]
                    return b, w

def exist(sol, v):
                    x=False
                    for i in range(len(sol)):
                                        if sol[i]==v:
                                                            x=True
                    return x

def SortAccordingEff(s, sim):
                    profit=s[1]
                    s=s[0]
                    sol=[]
                    for i in range(len(sim)):
                                        if exist(s, sim[i]):
                                                            sol.append(sim[i])
                    return [sol, profit]

def create_sol(items, k):
                    sol=[]
                    r=random.randint(0, len(items)-1)
                    sol.append(r)
                    valid, sol, _=vr.greedy_verify(sol, items, k)
                    while valid:
                                        r=random.randint(0, len(items)-1)
                                        if exist(sol, r)==False:
                                                            sol.append(r)
                                                            valid, sol, _=vr.greedy_verify(sol, items, k)
                                                            if valid==False:
                                                                                sol.remove(r)
                    valid, sol, profit=vr.greedy_verify(sol, items, k)
                    sol=[sol, profit]
                    sim=eff.simple()
                    sol=SortAccordingEff(sol, sim)
                    return sol

def subject():
                    items, cap=ctl.main()
                    k=knapsack(cap)
                    pickle_out=open(info.sub_path, 'wb')
                    pickle.dump([items, k], pickle_out)

def create(third):
                    r=random.choice(third)
                    valid, sol=vr.verify([r])
                    sol=sol[0]
                    while valid:
                                        r=random.choice(third)
                                        if exist(sol, r)==False:
                                                            sol.append(r)
                                                            valid, sol=vr.verify(sol)
                                                            sol=sol[0]
                                                            if valid==False:
                                                                                sol.remove(r)
                    valid, sol=vr.verify(sol)
                    return sol

def greedy():
                    #Create 500 randomly solutions and verify them using the function "verify"
                    #And save them in pickle file
                    #Sort the solutions acording the efficiency list
                    #The solutions which in first quarter of the solutions list are from the first third of the efficincy list
                    sc=eff.simple()
                    r=len(sc)//3
                    rr=(len(sc)//3)*2
                    third=sc[:r]
                    med_third=sc[r:rr]
                    low=sc[rr:]
                    solutions=[]
                    for i in range(125):
                                       solutions.append(create(third))

                    for i in range(125):
                                        solutions.append(create(med_third))

                    for i in range(125):
                                        solutions.append(create(low))

                    for i in range(125):
                                        solutions.append(create(sc))

                    b, w=BestAndWorst(solutions)
                    valid, b=vr.verify(b[0])
                    print(valid, b)

                    pickle_out=open(info.sol_path, 'wb')
                    pickle.dump(solutions, pickle_out)



def main():
                    subject()
                    greedy()

main()
