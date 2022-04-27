import genetic_algo as GA
import recherche_locale as rl
import verify as vr
import info
import pickle
import efficiency as eff
import random
import time

def exist(sol, v):
                    x=False
                    for i in range(len(sol)):
                                        if sol[i]==v:
                                                            x=True
                    return x


def processing(solutions, i):

                    print('Generation number=', i)

                    """solutions=ACO.main(solutions)
                    b, _=vr.BestAndWorst(solutions)
                    valid, b=vr.verify(b[0])
                    print('ACO:', valid, b[1])"""
                    
                    solutions=GA.main(solutions)
                    b, _=vr.BestAndWorst(solutions)
                    valid, b=vr.verify(b[0])
                    print('Genetic A:', valid, b[1])

                    
                    bb=rl.neighborhood(b)
                    print('Local S:', valid, b[1])
                   
                    for i in range(len(solutions)):
                                        if solutions[i]==b:
                                                            solutions[i]=bb
                    return solutions

def main():
                    pickle_in=open(info.sol_path, 'rb')
                    solutions=pickle.load(pickle_in)

                    print('Population')
                    b, _=vr.BestAndWorst(solutions)
                    print('Best solu=', b[1])
                    print('population size=', len(solutions))

                    for i in range(10):
                                                        solutions=processing(solutions, i+1)
                    
                    b, _=vr.BestAndWorst(solutions)
                    valid, b=vr.verify(b[0])
                    print(valid, b)
                    


start=time.time()
main()
end=time.time()

print('running time=', round(end-start, 2))
                    
