import info
import pickle
import efficiency as eff
import random
import verify as vr

def statistics(sol):
                    sc=eff.scaled()
                    print(len(sc))
                    th=(len(sc)//3)
                    sth=(len(sc)//3)*2

                    th_list=sc[:th]
                    sth_list=sc[th:sth]
                    tth_list=sc[sth:]

                    x1=0
                    core=0
                    x=0
                    for i in range(len(sol)):
                                        if exist(th_list, sol[i]):x1+=1
                                        if exist(sth_list, sol[i]):core+=1
                                        if exist(tth_list, sol[i]):x+=1

                    return x1, core, x



def exist(sol, v):
                    ex=False
                    for i in range(len(sol)):
                                        if sol[i]==v:
                                                            ex=True
                    return ex

def getRemainningItems(sol):
                    #Load the items list
                    pickle_in=open(info.sub_path, 'rb')
                    items, _=pickle.load(pickle_in)

                    restItems=[]
                    for i in range(len(items)):
                                        if exist(sol, i)==False:
                                                            restItems.append(i)

                    return restItems

def getRemainningResource(a):
                    rc, cap=vr.getRC(a)
                    
                    rest=[]
                    for i in range(len(rc)):
                                        rest.append(0)

                    for i in range(len(rc)):
                                        rest[i]=int(cap[i])-rc[i]
                    
                    return rest

def SortAccordingEff(r, sim):
                    rr=[]
                    for i in range(len(sim)):
                                        if exist(r, sim[i]):
                                                            rr.append(sim[i])
                    return rr

def ant(sol, rest):

                    valid, sol=vr.verify(sol)
                    sol=sol[0]
                    p=[]
                    for i in range(len(rest)):
                                        if exist(sol, rest[i])==False:
                                                            sol.append(rest[i])
                                                            p.append(rest[i])
                                                            valid, sol=vr.verify(sol)
                                                            sol=sol[0]
                                                            if valid==False:
                                                                                sol.remove(rest[i])
                                                                                p.remove(rest[i])
                                                                                break
                    for i in range(len(p)):
                                        rest.remove(p[i])

                    valid, sol=vr.verify(sol)
                    return sol, rest

def ACO(sol):
                    s=sol
                    sol=sol[0]
                    trails=[]
                    sc=eff.scaled()
                    t=(len(sc)//3)*2
                    t=sc[t:]

                    #Remove the items that have low efficiency from the solution
                    for i in range(35):
                                        for i in range(len(t)):
                                                            if exist(sol, t[i]):
                                                                                sol.remove(t[i])
                                                                                break
                    
                    #Add a new items that have best efficiency to the solution
                    for i in range(10):
                                        trail, sc=ant(sol, sc)
                                        trails.append(trail)
                                        #print(i, '#len rest=', len(sc), trail[1])

                    b, _=vr.BestAndWorst(trails)
                    return b

def main(solutions):
                    s=solutions
                    b1, _=vr.BestAndWorst(solutions)
                    print(b1[1])
                    sols=[]
                    for i in range(len(solutions)):
                                        sols.append(ACO(solutions[i]))

                    #Remove the invalid solutions
                    f=[]
                    for i in range(len(sols)):
                                        valid, _=vr.verify(sols[i][0])
                                        if valid==False:
                                                            f.append(sols[i])

                    for i in range(len(f)):
                                        sols.remove(f[i])

                    b, _=vr.BestAndWorst(sols)
                    b1, _=vr.BestAndWorst(s)
                    if b[1]>=b1[1]:
                                        print(b[1], '>=', b1[1])
                                        return sols         
                    if b[1]<b1[1]:
                                        print(b[1], '<', b1[1])
                                        return s
                    

sol=[17, 23, 26, 28, 29, 34, 40, 41, 49, 56, 
61, 62, 65, 68, 73, 81, 84, 85, 92, 94, 98, 1, 78, 8, 31, 6, 76, 18, 72]
x1, core, x=statistics(sol)
print('statistics=', x1, core, x)
valid, sol=vr.verify(sol)
print(valid, sol)
