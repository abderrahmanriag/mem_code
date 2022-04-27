from random import randrange
import info
import pickle

def avg(items):
                    dims=[]
                    for i in range(len(items[1].resource)):
                                        dim=[]
                                        for j in range(len(items)):
                                                            dim.append(items[j].resource [i])
                                        dims.append(dim)                                     

def main():
                    pickle_in=open(info.sub_path, 'rb')    
                    items, k=pickle.load(pickle_in)

