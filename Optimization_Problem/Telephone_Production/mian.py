#frist import the model class from docplex.mp
from unicodedata import name
from docplex.mp.model import Model

#create one model instance, with a name
m=Model(name='telephone_production')

#by default, all variables in doplex have a lower bound of 0 and infinit upper bound
desk=m.continuous_var(name='desk')
cell=m.continuous_var(name='cell')

#write constraints
#constraint #1: desk production is greater then 100
m.add_constraint(desk>=100)

#constraint #2: cell production is greater then 100
m.add_constraint(cell>=100)

#constraint #3: assembly time limit
ct_assembly=m.add_constraint(0.2*desk+0.4*cell<=400)

#constraint #4: painting time limit
ct_painting=m.add_constraint(0.5*desk+0.4*cell<=490)

#The objective
m.maximize(12*desk+20*cell)

m.print_information()

s=m.solve()
m.print_solution()