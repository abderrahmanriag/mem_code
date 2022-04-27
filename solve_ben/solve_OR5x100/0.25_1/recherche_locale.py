from selectors import BaseSelector
import info
import pickle
import efficiency as eff
import random
import verify as vr


def getRemainningItems(sol):
                    #Load the items list
                    pickle_in=open(info.sub_path, 'rb')
                    items, _=pickle.load(pickle_in)

                    restItems=[]
                    for i in range(len(items)):
                                        if exist(sol, i)==False:
                                                            restItems.append(i)
                    
                    sim=eff.scaled()
                    restItems=SortAccordingEff(restItems, sim)
                    return restItems

def exist(sol, v):
                    x=False
                    for i in range(len(sol)):
                                        if sol[i]==v:
                                                            x=True
                    return x

def SortAccordingEff(s, sim):
                    sol=[]
                    for i in range(len(sim)):
                                        if exist(s, sim[i]):
                                                            sol.append(sim[i])
                    return sol

def hhhhhhhhh(sol):
                    sol=sol[0]

                    sim_eff=eff.simple()
                    r=(len(sim_eff)//2)

                    h=[]
                    for i in range(len(sol)):
                                     if exist(sim_eff[r:], sol[i]):h.append(sol[i])

                    for i in range(len(h)):
                                        sol.remove(h[i])
                    
                    r=len(sim_eff)//3

                    for i in range(len(sim_eff[:r])):
                                        if exist(sol, sim_eff[i])==False:
                                                            sol.append(sim_eff[i])
                                                            valid, sol=vr.verify(sol)
                                                            sol=sol[0]
                                                            if valid==False:
                                                                                sol.remove(sim_eff[i])
                    
                    valid, sol=vr.verify(sol)
                    return sol

def hill(sol):
                    s=sol
                    sol=sol[0]
                    sc=eff.scaled()
                    th=(len(sc)//3)*2

                    #Get the first third of the eff list
                    th=sc[th:]
                    oth=len(sc)//3

                    #Get the last third of the eff list
                    oth=sc[:oth]


                    for i in range(len(th)):
                                        r=th[i]
                                        if exist(sol, r):
                                                            sol.remove(r)

                    
                    _, sol=vr.verify(sol)
                    if sol[1]>=s[1]:
                                        return sol
                    if s[1]>=sol[1]:                                        
                                        return s

def hill1(sol):
                    s=sol
                    sol=sol[0]
                    sc=eff.scaled()
                    #Get the last third of the eff list
                    th=(len(sc)//3)*2
                    th=sc[th:]

                    #Get the first third of the eff list
                    oth=len(sc)//3
                    oth=sc[:oth]

                    for i in range(len(oth)):
                                        r=oth[i]
                                        if exist(sol, r)==False:
                                                            sol.append(r)
                                        valid, sol=vr.verify(sol)
                                        sol=sol[0]
                                        if valid==False:
                                                            sol.remove(r)
                    _, sol=vr.verify(sol)
                    if sol[1]>=s[1]:
                                        return sol
                    if s[1]>=sol[1]:
                                        return s

def hill_climbing(sol):
                    sol=sol[0]
                    sc=eff.scaled()
                    r=random.choice(sc)
                    if exist(sol, r)==False:
                                        sol.append(r)
                    valid, sol=vr.verify(sol)
                    sol=sol[0]
                    if valid==False:
                                        sol.remove(r)
                    valid, sol=vr.verify(sol)
                    return sol

def change(sol, v):
                    mat=[]
                    rest=getRemainningItems(sol)
                    sol.remove(v)
                    for i in range(len(rest)):
                                        sol.append(rest[i])
                                        valid, sol=vr.verify(sol)                                        
                                        if valid:mat.append(sol)
                                        sol=sol[0]
                                        sol.remove(rest[i])
                    sol.append(v)
                    """for i in range(len(mat)):
                                        print(mat[i][1])"""
                    
                    return mat

def neighborhood(sol):
                    neighbors=[]
                    sol=sol[0]
                    for i in range(len(sol)):
                                        mat=change(sol, sol[i])
                                        if len(mat)!=0:
                                                            for i in range(len(mat)):
                                                                                neighbors.append(mat[i])
                    b, _=vr.BestAndWorst(neighbors)
                    return b

def main(solutions):
                    _, b=vr.BestAndWorst(solutions)
                    print(b[1])
                    print(neighborhood(b)[1])
                    solutions.remove(b)

                    _, b=vr.BestAndWorst(solutions)
                    print(b[1])
                    print(neighborhood(b)[1])      


