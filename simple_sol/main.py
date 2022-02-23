from object import *
from knapsack import *
from solving import *
#create a knapsack instance
k=knapsack(2, [10, 12])
#create the list of objects
items=[]
o1=item([3, 2], 17);items.append(o1)
o2=item([4, 5], 16);items.append(o2)
o3=item([4, 3], 16);items.append(o3)
o4=item([3, 3], 17);items.append(o4)
get_randomly_solutions(items, k)