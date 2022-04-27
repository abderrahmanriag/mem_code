from random import *
from knapsack import knapsack
def main():
    outfile=open('benchmark.txt', 'w')

    print('Creating intances...')
    n=100       #number of items
    m=5          #constraints or knapsack dim
    cap=[]
    for i in range(m):
        cap.append(randint(5, 8))
    print(cap)
    k=knapsack(m, cap)
    k.show()

    outfile.write(k)
main()