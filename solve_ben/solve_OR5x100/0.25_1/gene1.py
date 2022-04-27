import pickle
import info
import random
import verify as vr

def bit(sol):
                    sol=sol[0]
                    pickle_in=open(info.sub_path, 'rb')
                    items, _=pickle.load(pickle_in)
                    s=[]
                    for i in range(len(items)):
                                        s.append(0)
                    for i in range(len(sol)):
                                        s[sol[i]]=1

                    return s

def crossover(a, b, j, q):
                    offspring=[]
                    for i in range(j, q):
                                        a[i], b[i]=b[i], a[i]

                    va, a=vr.verifyBit(a)
                    vb, b=vr.verifyBit(b)
                    if va:offspring.append(a)
                    if vb:offspring.append(b)

                    return offspring

def operations(solutions):
                    #Create the list for saving the produced solutions "offspring"
                    offspring=[]
                    a=random.choice(solutions)
                    b=random.choice(solutions)
                    while b==a:
                                        b=random.choice(solutions)

                    a=bit(a)
                    b=bit(b)

                    #Single point crossover
                    r=random.randint(0, len(a)-1)

                    off=crossover(a, b, r, len(a))

                    if len(off)!=0:
                                        for i in range(len(off)):
                                                            offspring.append(off[i])

                    off=[]
                    #Two point crossover
                    j=random.randint(0, len(a)-1)
                    q=random.randint(j, len(a)-1)

                    off=crossover(a, b, j, q)
                    if len(off)!=0:
                                        for i in range(len(off)):
                                                            offspring.append(off[i])

                    return offspring

                    
                    
def main(solutions):
                    b, _=vr.BestAndWorst(solutions)
                    valid, b=vr.verify(b[0])
                    print(valid, ' #', b[1])

                    offspring=[]
                    for i in range(100):
                                        off=operations(solutions)
                                        if len(off)!=0:
                                                            for i in range(len(off)):
                                                                                offspring.append(off[i])

                    b, _=vr.BestAndWorst(offspring)
                    valid, b=vr.verify(b[0])
                    print(valid, ' #', b[1])

import random
import info
import pickle
import verify as vr
import recherche_locale as local
import efficiency as eff

def getRemainningItems(sol):
                    #Load the items list
                    pickle_in=open(info.sub_path, 'rb')
                    items, _=pickle.load(pickle_in)

                    restItems=[]
                    for i in range(len(items)):
                                        if exist(sol, i)==False:
                                                            restItems.append(i)

                    return restItems

def exist(sol, v):
                    x=False
                    for i in range(len(sol)):
                                        if sol[i]==v:
                                                            x=True
                    return x

def CompleteCrossover(a, b):
                    h=len(b)
                    for i in range(len(b), len(a)):
                                        b.append(a[i])
                    for i in range(h, len(b)):
                                        a.remove(b[i])
                    return a, b

def reSort(s):
                    profit=s[1]
                    s=s[0]
                    l=len(s)-1
                    sol=[]
                    for i in range(len(s)):
                                        sol.append(s[l])
                                        l-=1
                    return [sol, profit]

def SortAccordingEff(s):
                    sim=eff.scaled()
                    sol=[]
                    for i in range(len(sim)):
                                        if exist(s, sim[i]):
                                                            sol.append(sim[i])
                    return sol

def mutation(sol):
                    s=sol
                    sol=sol[0]
                    rest=getRemainningItems(sol)
                    rest=SortAccordingEff(rest)
                    for i in range(len(rest)):
                                        sol.append(rest[i])
                                        valid, sol=vr.verify(sol)
                                        sol=sol[0]
                                        if valid==False:
                                                            sol.remove(rest[i])
                    
                    valid, sol=vr.verify(sol)
                    if s[1]<=sol[1]:
                                        return sol
                    else:
                                        return s
                    
def crossover(a, b, x, y):

                    #Create list offspring for saving produced solutions
                    offspring=[]

                    if y==len(b):
                                        f=a[y:]
                                        for i in range(len(f)):
                                                            a.remove(f[i])
                                        for i in range(x, y):
                                                            a[i], b[i]=b[i], a[i]
                                        for i in range(len(f)):
                                                            b.append(f[i])
                    else:
                                        for i in range(x, y):
                                                            a[i], b[i]=b[i], a[i]
                    
                    a=sorted(set(a))
                    b=sorted(set(b))

                    va, a=vr.verify(a)
                    vb, b=vr.verify(b)

                    if va:
                                        offspring.append(a)
                    if vb:
                                        offspring.append(b)

                    return offspring

"""def genetic_algorithm(solutions):


                    offspring=[]

                    #Define number of operations
                    np=20

                    #Single point crossover
                    single_offspring=[]

                    for i in range(np):
                                        a=random.choice(solutions)
                                        b=random.choice(solutions)
                                        while b==a:
                                                            b=random.choice(solutions)

                                        a=reSort(a)
                                        a=a[0]
                                        b=b[0]
                                        m=min(len(a), len(b))

                                        #Crossover point
                                        j=random.randint(0, m-1)
                                        if len(a)>=len(b):
                                                            so=crossover(a, b, j, m)
                                        else:
                                                            so=crossover(b, a, j, m)
                                        if len(so)!=0:
                                                            for i in range(len(so)):
                                                                                single_offspring.append(so[i])


                    #Two points crossover
                    two_offspring=[]

                    for i in range(np):
                                        a=random.choice(solutions)
                                        b=random.choice(solutions)
                                        while b==a:
                                                            b=random.choice(solutions)
                                        
                                        a=reSort(a)
                                        a=a[0]
                                        b=b[0]
                                        m=min(len(a), len(b))

                                        j=random.randint(0, m-1)
                                        q=random.randint(j, m-1)

                                        tp=crossover(a, b, j, q)

                                        if len(tp)!=0:
                                                            for i in range(len(tp)):
                                                                                two_offspring.append(tp[i])




                    for i in range(len(single_offspring)):
                                        offspring.append(single_offspring[i])

                    for i in range(len(two_offspring)):
                                        offspring.append(two_offspring[i])





                    
                    m=[]
                    for i in range(len(offspring)):
                                        m.append(mutation(offspring[i]))

                    for i in range(len(m)):
                                        offspring.append(m[i])

                    return offspring                    

def gen_algo(best_eff, med_eff):
                    offspring=[]

                    #Define number of operations
                    np=20

                    #Single point crossover
                    single_offspring=[]

                    for i in range(np):
                                        a=random.choice(best_eff)
                                        b=random.choice(med_eff)
                                        

                                        a=reSort(a)
                                        a=a[0]
                                        b=b[0]
                                        m=min(len(a), len(b))

                                        #Crossover point
                                        j=random.randint(0, m-1)
                                        if len(a)>=len(b):
                                                            so=crossover(a, b, j, m)
                                        else:
                                                            so=crossover(b, a, j, m)
                                        if len(so)!=0:
                                                            for i in range(len(so)):
                                                                                single_offspring.append(so[i])


                    #Two points crossover
                    two_offspring=[]

                    for i in range(np):
                                        a=random.choice(best_eff)
                                        b=random.choice(med_eff)
                                        
                                        
                                        a=reSort(a)
                                        a=a[0]
                                        b=b[0]
                                        m=min(len(a), len(b))

                                        j=random.randint(0, m-1)
                                        q=random.randint(j, m-1)

                                        tp=crossover(a, b, j, q)

                                        if len(tp)!=0:
                                                            for i in range(len(tp)):
                                                                                two_offspring.append(tp[i])




                    for i in range(len(single_offspring)):
                                        offspring.append(single_offspring[i])

                    for i in range(len(two_offspring)):
                                        offspring.append(two_offspring[i])





                    
                    m=[]
                    for i in range(len(offspring)):
                                        m.append(mutation(offspring[i]))

                    for i in range(len(m)):
                                        offspring.append(m[i])

                    return offspring                    
"""

def main(solutions):

                    b=len(solutions)//4
                    best_eff=solutions[:b]

                    m=(len(solutions)//4)*2
                    med_eff=solutions[b: m]

                    offspring=genetic_algorithm(solutions)

                    for i in range(len(offspring)):
                                        sol=offspring[i]
                                        valid, sol=vr.verify(sol[0])
                                        if valid:
                                                            solutions.append(offspring[i])

                                        
                    offspring=gen_algo(best_eff, med_eff)

                    for i in range(len(offspring)):
                                        sol=offspring[i]
                                        valid, sol=vr.verify(sol[0])
                                        if valid:
                                                            solutions.append(offspring[i])

                    f=[]
                    for i in range(len(solutions)):
                                        valid, b=vr.verify(solutions[i][0])
                                        if valid==False:
                                                            f.append(solutions[i])

                    for i in range(len(f)):
                                        solutions.remove(f[i])
                    return solutions
 