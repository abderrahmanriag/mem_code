import info
import pickle
import verify as vr
import random
import time
import efficiency as eff

def SortAccordingEff(sol):
                    sol=sol[0]
                    s=[]
                    scaled=eff.scaled()
                    for i in range(len(scaled)):
                                        if vr.exist(sol, scaled[i]):
                                                            s.append(scaled[i])
                    return s

def tournament(solutions, tour):
                    #The winners for the tournament will be candidates to crossover operation
                    winners=[]
                    #Create a list for saving the rest of the solutions
                    rest=[]
                    print(tour, len(solutions))
                    for i in range(len(solutions)//tour):
                                        tour_list=[]
                                        for i in range(tour):
                                                            r=random.choice(solutions)
                                                            solutions.remove(r)
                                                            tour_list.append(r)
                                        b, _=vr.BestAndWorst(tour_list)
                                        winners.append(b)
                                        tour_list.remove(b)
                                        for i in range(len(tour_list)):
                                                            rest.append(tour_list[i])
                    return winners, rest

def crossover(a, b, x, y):
                    #Define the list of the produced solutions "offspring"
                    offspring=[]

                    #Swap the genes between x and y
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
                    
                    #Remove the repetetion from the produces solutions
                    a=sorted(set(a))
                    b=sorted(set(b))

                    va, a=vr.verify(a)
                    vb, b=vr.verify(b)

                    if va:offspring.append(a)
                    if vb:offspring.append(b)

                    return offspring

def flip(sol):
                    sol=sol[0]
                    rest=vr.getRemainingItems(sol)
                    rest=SortAccordingEff(rest)
                    for i in range(len(rest)):
                                        sol.append(rest[i])
                                        valid, sol=vr.verify(sol)
                                        sol=sol[0]
                                        if valid:sol.remove(rest[i])

                    valid, sol=vr.verify(sol)
                    return sol

def mutation(winners):
                    results=[]
                    for i in range(len(winners)):
                                        result=flip(winners[i])
                                        results.append(result)
                    return results

def operation(solutions, pc, pm):
                    generation=[]

                    #population size=length of  the population "solutions"

                    #Crossover
                    #Get the candidates according the crossover probability
                    #number of candidates=pc/population size
                    cand=pc*len(solutions)
                   

                    #tournament size=population size/number of candidates
                    tour=len(solutions)//cand

                    winners, solutions=tournament(solutions, tour)
                    #Create a list for new generation
                    offspring=[]

                    for i in range(100):

                                        #Select two solutions randomly from winners list
                                        a=random.choice(winners)
                                        b=random.choice(winners)
                                        while b[1]!=a[1]:
                                                            b=random.choice(winners)

                                        #The solution's structure -> 1)the list of contained items 2)the profit "fitness"
                                        #Each items contained in the solution is expressed by its order in the list of  items 
                                        
                                        #Get the list of contained items in the solution
                                        a=a[0]
                                        b=b[0]

                                        #Get the minimum length between two selected solutions
                                        m=min(len(a), len(b))

                                        #Single Point Crossover
                                        j=random.randint(0, m)

                                        #done=True whene the crossover is finished
                                        done=False

                                        if m==len(a):
                                                            child=crossover(b, a, j, m)
                                                            done=True
                                        if m==len(b) and done==False:
                                                            child=crossover(a, b, j, m)

                                        if len(child)!=0:
                                                            for i in range(len(child)):
                                                                                offspring.append(child[i])

                    for i in range(len(offspring)):
                                        generation.append(offspring[i])


                    #Mutation
                    #Get the candidates according the mutation probability
                    #number of candidates=pm/population size
                    #Update the probability of the mutation
                    pm=pm+(pc/2)
                    cand=pm*len(solutions)

                    #tournament size=population size/number of candidates
                    tour=len(solutions)//cand

                    winners, solutions=tournament(solutions, tour)
                    results=mutation(winners)

def main():        
                    #Load the solutions list
                    pickle_in=open(info.sol_path, 'rb')
                    solutions=pickle.load(pickle_in)

                    b, _=vr.BestAndWorst(solutions)
                    valid, b=vr.verify(b[0])
                    print(valid, b[1])
                   
                    #Crossover probability -> 
                    # the probability of  Choosing some solutions to be candidates to crossover function
                    pc=0.2
                    print('pc=', pc)
                    #Mutation probability
                    #the probability of Choosing some solutions to be candidates to mutation operation
                    pm=0.7
                    print('pm=', pm)
                    print('Update pm # pm=pm+(pc/2)')
                    pc=pc/2
                    print('pc/2=', pc)
                    pm=pm+(pc)
                    pm=round(pm, 1)
                    print(pm)
                    #Reproduction probability
                    #the probability of Choosing some solutions to be candidates to reproduction operation
                    pr=0.1

                    """offspring=operation(solutions, pc, pm, pr)

                    b, _=vr.BestAndWorst(offspring)

                    valid, b=vr.verify(b[0])
                    print(valid, b[1])"""

pickle_in=open(info.sol_path, 'rb')
solutions=pickle.load(pickle_in)

b, _=vr.BestAndWorst(solutions)

valid, b=vr.verify(b[0])
print(valid, b[1])