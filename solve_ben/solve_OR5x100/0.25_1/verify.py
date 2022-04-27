import pickle
import info

def verify(sol):
    pickle_in=open(info.sub_path, 'rb')
    items, k=pickle.load(pickle_in)
    cap=k.capacities
    rc, profit=objective(sol, items, len(cap))
    #print_info(sol)
    for i in range(len(cap)):
        if(rc[i]<=int(cap[i])):
            valid=True
        else:
            valid=False
            break
    sol=[sol, profit]
    return valid, sol

def objective(sol, items, cap):
    if items==[]:
        pickle_in=open(info.sub_path, 'rb')
        items, _=pickle.load(pickle_in)
    rc=[]
    for i in range(cap):
        rc.append(0)
    profit=0
    for i in range(len(sol)):
        for j in range(cap):
            rc[j]=rc[j]+int(items[sol[i]].resource[j])
        profit=profit+int(items[sol[i]].profit)
    return rc, profit

def getRC(sol):
    pickle_in=open(info.sub_path, 'rb')
    items, k=pickle.load(pickle_in)

    if len(sol)==2:sol=sol[0]
    cap=k.capacities
    rc, _=objective(sol, items, len(cap))
    return rc, cap

def print_info(sol):
    pickle_in=open(info.sub_path, 'rb')
    items, k=pickle.load(pickle_in)
    cap=k.capacities
    rc, profit=objective(sol, items, len(cap))
    print('rc=', rc)
    print('cap=', k.capacities)
    print('profit=', profit)

def BestAndWorst(solutions):
                    sol=[]
                    for i in range(len(solutions)):
                                        sol.append(solutions[i][1])
                    b=sol.index(max(sol))
                    b=solutions[b]
                    w=sol.index(min(sol))
                    w=solutions[w]
                    return b, w

def chromosome(sol):
    s=[]
    for i in range(len(sol)):
        if sol[i]==1:
            s.append(i)
    return s

def bit(sol):
                    pickle_in=open(info.sub_path, 'rb')
                    items, _=pickle.load(pickle_in)
                    s=[]
                    for i in range(len(items)):
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

def getRemainingItems(sol):
    pickle_in=open(info.sub_path, 'rb')
    items, _=pickle.load(pickle_in)

    rest=[]
    for i in range(len(items)):
        if exist(sol, i)==False:rest.append(i)

    return rest

