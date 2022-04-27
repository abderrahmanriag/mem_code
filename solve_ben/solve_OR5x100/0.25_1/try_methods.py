import verify as vr
import info
import pickle
import random
import time

def crossover(a, b, x, y):
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


                    return a, b

def mainchro():
                    pickle_in=open(info.sol_path, 'rb')
                    solutions=pickle.load(pickle_in)
                    a=random.choice(solutions)
                    b=random.choice(solutions)

                    print(a[1], '#', b[1])
                    a=a[0]
                    b=b[0]
                    m=min(len(a), len(b))
                    print('len a=', len(a), 'len b=', len(b), 'm=', m)
                    done=False
                    if m==len(a):
                                        print('len a=', len(a), '=m=', m)
                                        b, a=crossover(b, a, 2, m)
                                        done=True
                    if m==len(b) and done==False:
                                        print('len b=', len(b), '=m=', m)
                                        print(len(a))
                                        a, b=crossover(a, b, 2, m)

                    va, a=vr.verify(a)
                    vb, b=vr.verify(b)
                    print(va, a[1], '#', vb, b[1])
t=[]
for i in range(100):
                    start=time.time()
                    mainchro()
                    end=time.time()
                    run=end-start
                    t.append(run)

m=max(t)
mi=min(t)

print(m, '#', mi)