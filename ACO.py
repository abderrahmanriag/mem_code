from random import *
def ACO(items, knapsack):
    for i in range(len(items)):
        item1=randint(0, len(items)-1)
        #print('The selected item is o', selected_ob+1, ' And its informations:') 
        #items[selected_ob].show()
        cond=items[:item1]+items[item1+1:]
        while (cond!=[]):
            item2=randint(0, len(cond)-1)
            if(item1.resource[0]+item2.resource[0]<=knapsack.capacities[0]
            and item1.resource[1]+item2.resource[1]<=knapsack.capacities[1]):
                pass