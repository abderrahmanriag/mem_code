'''
    a funiture company has create tables and chairs,
    each table requires 4 hours for carpentry,
    and 2 hours for painting, and yeild E7
    each chair requires 3 hours for carpentry,
    and 1 hour for painting, and yeild E5
    we have 240 hours, 
    how many tables and chairs we should create to get the maximum profit?
'''
from docplex.mp.model import Model

m=Model(name='funiture_company')

table=m.continuous_var(name='table')
chair=m.continuous_var(name='chair')

m.add_constraint(table>=0)
m.add_constraint(chair>=0)

m.add_constraint(4*table+3*chair<=240)
m.add_constraint(2*table+chair<=100)

m.maximize(7*table+5*chair)

m.print_information

m.solve()
m.print_solution()