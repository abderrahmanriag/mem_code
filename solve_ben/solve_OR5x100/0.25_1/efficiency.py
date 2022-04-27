import info
import pickle

def simple():
                    pickle_in=open(info.sub_path, 'rb')
                    items, _=pickle.load(pickle_in)

                    sim_eff=[]
                    for i in range(len(items)):
                                        s=0
                                        for j in range(len(items[i].resource)):
                                                            s=s+int(items[i].resource[j])
                                        d=int(items[i].profit)/s
                                        d=(round(d, 2))
                                        sim_eff.append(d)
                    for i in range(len(sim_eff)):
                                        sim_eff[i]=[sim_eff[i], i]
                    sim_eff.sort(reverse=True)
                    for i in range(len(sim_eff)):
                                        sim_eff[i]=sim_eff[i][1]
                    return sim_eff

def scaled():
                    #Load the subject
                    pickle_in=open(info.sub_path, 'rb')
                    items, k=pickle.load(pickle_in)

                    sc_eff=[]
                    cap=k.capacities
                    for i in range(len(items)):
                                        s=0
                                        for j in range(len(cap)):
                                                            s=s+int(items[i].resource[j])/int(cap[j])
                                        d=int(items[i].profit)/s
                                        d=(round(d, 2))
                                        sc_eff.append(d)
                    for i in range(len(sc_eff)):
                                        sc_eff[i]=[sc_eff[i], i]
                    sc_eff.sort(reverse=True)
                    for i in range(len(sc_eff)):
                                        sc_eff[i]=sc_eff[i][1]
                    return sc_eff

           