import pickle
import random
import verify as vr
import efficiency as eff
import local_search as lc
import info

def bit(sol, len_items):
    if(len(sol)==2):
        sol=sol[0]
    s=[]
    for i in range(len_items):
        s.append(0)
    for i in range(len(sol)):
        s[sol[i]]=1
    return s

def exist(sol, o):
    ex=False
    for i in range(len(sol)):
        if(sol[i]==o):
            ex=True
    return ex

def max_and_min(solutions):
    b=solutions[0]
    for i in range(len(solutions)):
        if(b[1]<=solutions[i][1]):
            b=solutions[i]
    w=solutions[0]
    for i in range(len(solutions)):
        if(w[1]>=solutions[i][1]):
            w=solutions[i]
    return b, w

def re_sort(sol, items, k):
    s=[]
    sc=eff.scaled(items, k)
    for i in range(len(sc)):
        sc[i]=sc[i][1]
    for i in range(len(sc)):
        if exist(sol, sc[i]):
            s.append(sc[i])
    return s

def spc_change(l, j, k):
    a=l[0]
    b=l[1]

    for i in range(j, k):
        a[i], b[i]=b[i], a[i]
    
    va, a=vr.verify([a, 0])
    vb, b=vr.verify([b, 0])

    if va:
        l[0]=a
    if vb:
        l[1]=b
    return l
    
def single_point_crossover(a, b, items):

    #Create a list children for saving the produced solutions
    children=[]

    #A crossover point on the parent organism string is selected. 
    # All data beyond that point in the organism string is swapped between the two parent organisms.
    if len(a)>=len(b):r=random.randint(0, len(a)-1)
    else:r=random.randint(0, len(b)-1)
    print('Crossover point=', r)

    #These lists to save the deleted items from the parents
    rep=[]
    rep1=[]

    #Remove all items that great or equal then "r" from the solution "a"
    for i in range(len(a)):
        if a[i]>=r:rep.append(a[i])
    for i in range(len(rep)):a.remove(rep[i])
    
    #Put the items that great or equal then "r" from "b" to "a"
    for i in range(len(b)):
        if b[i]>=r:
            a.append(b[i])
    
    #Remove all items that great or equal then "r" from "b"
    for i in range(len(b)):
        if b[i]>=r:rep1.append(b[i])
    for i in range(len(rep1)):b.remove(rep1[i])

    #Put the removed items from "a" in "b"
    for i in range(len(rep)):
        b.append(rep[i])

    va, a=vr.verify([a, 0])
    vb, b=vr.verify([b, 0])

    if va:children.append(a)
    if vb:children.append(b)

    return children

def two_point_crossover(a, b, len_items):
    
    #Change the form of the solution to the bit
    a=bit(a, len_items)
    b=bit(b, len_items)

    #Create a list children for saving the produced solutions
    children=[]

    #A crossover point on the parent organism string is selected. 
    # All data beyond that point in the organism string is swapped between the two parent organisms.
    r=random.randint(0, max(len(a), len(b))-1)
    rr=random.randint(r, max(len(a), len(b))-1)
    print('First crossover point=', r)
    print('Second crossover point=', rr)

    for i in range(r, rr):
        a[i], b[i]=b[i], a[i]

    va, a=vr.verify([a, 0])
    vb, b=vr.verify([b, 0])

    print(va, 'a=', a)
    print(vb, 'b=', b)

    """if va:children.append(a)
    if vb:children.append(b)

    return children"""

def crossover(a, b, j, k, len_items):

    #Create a list children for saving the produced solutions
    children=[]

    #Convert the solution structure into the bit
    a=bit(a, len_items)
    b=bit(b, len_items)

    # interchanging the genes
    for i in range(j, k):
        a[i], b[i]=b[i], a[i]
    
    #Verify the produced solutions
    va, a=vr.verify([a, 0])
    vb, b=vr.verify([b, 0])

    if va:children.append(a)
    if vb:children.append(b)

    return children

def crossover2(a, b, sc):
    print('a=', a)
    print('b=', b)

    a=a[0]
    b=b[0]

    #The idea is :
    #Interchanging some items from "a" to "b" according the "sc" list sorting

    #Define the edge of swapping
    r=(len(sc)//2)
    #Put the removed items of "a" on "ga" list to save them
    ga=[]
    for i in range(len(b)):
        if exist(sc[r:], b[i]):
            ga.append(b[i])
    
    #Put the removed items of "b" on "gb" list to save them
    gb=[]
    r=(len(sc)//2)
    for i in range(len(a)):
        if exist(sc[:r], a[i]):
            ga.append(a[i])

    #Append all the items inside the "ga" list to the solution "b" and verify it
    for i in range(len(ga)):
        b.append(ga[i])
        vb, b=vr.verify([b, 0])
        b=b[0]
        if vb==False:b.remove(ga[i])

    #Append all the items inside the "gb" list to the solution "a" and verify it
    for i in range(len(gb)):
        a.append(gb[i])
        va, a=vr.verify([a, 0])
        a=a[0]
        if va==False:a.remove(gb[i])

    va, a=vr.verify([a, 0])
    vb, b=vr.verify([b, 0])
    print('a=', a)
    print('b=', b)

def re_sort(sol, sc):
    a=[]
    for i in range(len(sc)):
        if exist(sol, sc[i]):a.append(sc[i])
    return a

def complete_crossover(j, k):
    h=len(k)
    for i in range(len(k), len(j)):
        k.append(j[i])
    for i in range(h, len(k)):
        j.remove(k[i])
    
    return j, k

def crossover_chromosom(a, b, j, k):

    #Create a list children for saving the produced solutions
    children=[]

    # interchanging the genes
    for i in range(j, k):
        a[i], b[i]=b[i], a[i]

    #Complete the ineterchanging
    if len(a)>=len(b):
        a, b=complete_crossover(a, b)
    else:
        b, a=complete_crossover(b, a)
    
    va, a=vr.verify([a, 0])
    vb, b=vr.verify([b, 0])

    if va:children.append(a)
    if vb:children.append(b)

    return children

def main(solutions, items, k):

    #Load  the efficiency list
    sc=eff.simple(items)
    for i in range(len(sc)):
        sc[i]=sc[i][1]


    #Number of operations "h"
    h=100

    #Single point crossoveri
    spc_offspring=[]

    #a1, b1=max_and_min(solutions)
    for i in range(h):
        a=random.choice(solutions)
        b=random.choice(solutions)

        #Sort the selected solution according the efficiency list 
        a=re_sort(a[0], sc)
        b=re_sort(b[0], sc)

        m=min(len(a), len(b))

        #Crossover point
        j=random.randint(0, m-1)
        q=random.randint(j, m-1)

        ch=crossover_chromosom(a, b, j, m)
        if len(ch)!=0:
            for i in range(len(ch)):
                spc_offspring.append(ch[i])

    a, _=max_and_min(spc_offspring)

    print('Single point crossover')
    print('a=', a)

    #Two points crossover
    tpc_offspring=[]
    for i in range(h):
        a=random.choice(solutions)
        b=random.choice(solutions)

        #Sort the selected solution according the efficiency list 
        a=re_sort(a[0], sc)
        b=re_sort(b[0], sc)

        m=min(len(a), len(b))

        #Crossover point
        j=random.randint(0, m-1)
        q=random.randint(j, m-1)

        ch=crossover_chromosom(a, b, j, q)
        if len(ch)!=0:
            for i in range(len(ch)):
                tpc_offspring.append(ch[i])

    a, _=max_and_min(tpc_offspring)

    print('Two point crossover')
    print('a=', a)
    
    offspring=[]
    for i in range(len(spc_offspring)):
        offspring.append(spc_offspring[i])
    for i in range(len(tpc_offspring)):
        offspring.append(tpc_offspring[i])

    b, w=max_and_min(offspring)

    print('best offspring=', b)

    print('improve the solution using local search')
    b=lc.local_search(b, items, k)
    offspring.append(b)
    w=lc.local_search(w, items, k)
    offspring.append(w)

    best=lc.local_search(offspring[0], items, k)
    ii=0
    for i in range(1, len(offspring)):
        z=lc.local_search(offspring[i], items, k)
        if z[1]>best[1]:
            best=z
            ii=i

    print('ii=', ii)
    print('offspring[best]=', offspring[ii])
    print('best=', best)


#Load the solutions list
pickle_in=open(info.sol_path, 'rb')
solutions=pickle.load(pickle_in)
#Load the subject
pickle_in=open(info.sub_path, 'rb')
items, k=pickle.load(pickle_in)
main(solutions, items, k)