from docplex.mp.model import Model

m=Model(name='telephone_production')

desk=m.continuous_var(name='desk')
cell=m.continuous_var(name='cell')

