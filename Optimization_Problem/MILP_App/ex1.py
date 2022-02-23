from docplex.mp.model import Model

m=Model(name='m')

x=m.binary_var(name='x')
y=m.continuous_var(name='y', lb=0)
z=m.integer_var(name='z', lb=0)

#add constraints
c1=m.add_constraint(x+2*y+z<=4, ctname='c1')
c2=m.add_constraint(2*z+y<=5, ctname='c2')
c3=m.add_constraint(x+y>=1, ctname='c3')

m.maximize(2*x+y+3*z)

m.print_information()

m.solve()
m.print_solution()