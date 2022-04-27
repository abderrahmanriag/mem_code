import info
import random
import verify as vr


def crossover(a, b):
                    x=[]
                    ra=random.choice(a)
                    x.append(ra)
                    a.remove(ra)

                    rb=random.choice(b)
                    x.append(rb)
                    b.remove(rb)

                    valid, x=vr.verify(x)
                    x=x[0]

                    while valid:
                                        ra=random.choice(a)
                                        x.append(ra)
                                        a.remove(ra)

                                        rb=random.choice(b)
                                        x.append(rb)
                                        b.remove(rb)

                                        valid, x=vr.verify(x)
                                        x=x[0]
                                        if valid==False:
                                                            x.remove(ra)
                                                            x.remove(rb)
                                                            a.append(ra)
                                                            b.append(rb)
                    
def main(solutions):
                    offspring=[]

                    