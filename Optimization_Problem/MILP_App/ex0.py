from docplex.mp.model import Model

m=Model(name='model')

x1=m.continuous_var(name='x1', lb=0)
x2=m.integer_var(name='x2', lb=0)

m.add_constraint(2*x1+x2<=8)
m.add_constraint(5*x1+2*x2<=15)

m.maximize(8*x1+7*x2)

m.print_information()

m.solve()
m.print_solution()