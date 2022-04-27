
def bit(sol):
                    s=[]
                    for i in range(6):
                                        s.append(0)
                    for i in range(len(sol)):
                                        s[sol[i]]=1

                    return s

def crossoverbit(a, b, j, q):
                    a=bit(a)
                    b=bit(b)
                    for i in range(j, q):
                                        a[i], b[i]=b[i], a[i]

                    print(a)
                    print(b)

a=7.9999999
a=round(a)
print(a)