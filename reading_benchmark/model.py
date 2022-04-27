from knapsack import *
from object import *
from readb import melef
from edit_list import *
aster=melef.readlines()
print(aster[-1])
k=knapsack(5, edit(aster[-1]))