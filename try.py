"""a=' 11927 13727 11551 13056 13460'
print(a)
ra8m=0
cap=[]
for i in range(1, len(a)):
    if(a[i]==' '):
        cap.append(a[ra8m+1:i])
        ra8m=i
    if(i==len(a)-1):
        cap.append(a[ra8m+1:])
print(cap)
for i in range(1, 91, 15):
    print(i)
for  i in range(1, 5):
    print(i)"""


"""
def change(j, k, l):
    for i in range(j, k):
        l[i]=1
l=[]
for i in range(100):
    l.append(randint(0, 1))
print('List=', l)
for i in range(0, len(l), 10):
    change(i, i+10, l)
print('the changed list=', l)"""

"""
l=[]
for i in range(20):
    l.append(randint(0, 9))
m=l[0]
ml=[]
while len(ml)<=5:
    for i in range(len(l)):
        if(m<=l[i]):
            m=l[i]
    l.remove(m)
    ml.append(m)
print(ml)


# library to generate a random number
import random

# function for implementing the single-point crossover
def crossover(l, q):

# converting the string to list for performing the crossover
	l = list(l)
	q = list(q)

# generating the random number to perform crossover
	k = random.randint(0, 15)
	print("Crossover point :", k)

# interchanging the genes
	for i in range(k, len(s)):
		l[i], q[i] = q[i], l[i]
	l = ''.join(l)
	q = ''.join(q)
	print(l)
	print(q, "\n\n")
	return l, q

def main():
    # patent chromosomes:

    s = '1100110110110011'
    p = '1000110011011111'
    print("Parents")
    print("P1 :", s)
    print("P2 :", p, "\n")

    # function calling and storing the off springs for
    # next generation crossover
    for i in range(5):
        print("Generation ", i+1, "Childrens :")
        s, p = crossover(s, p)

for i in range(5, 15):
    print(i)
    """
import random
print(random.randint(5, 5))