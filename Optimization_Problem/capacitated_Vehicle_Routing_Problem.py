import numpy as np

rnd=np.random
rnd.seed()

n=10
Q=20
N=[i for i in range(1, n+1)]
V=[0]+N
q={i:rnd.randint(1, 10) for i in N} 

print('N=', N)
print('V=', V)
print('q=', q)

loc_x = rnd.rand(len(V))*200
loc_y = rnd.rand(len(V))*100

import matplotlib.pyplot as plt
plt.scatter(loc_x[1:], loc_y[1:], c='b')
for i in N:
    plt.annotate('$q_%d=%d$' % (i, q[i]), (loc_x[i]+2, loc_y[i]))
plt.plot(loc_x[0], loc_y[0], c='r', marker='s')
plt.axis('equal')