from sympy import *
import ast

#e.g. [[1,4,2,5],[3,6,4,1],[5,2,6,3]]
PD = input('Enter PD code:')

#python takes the input as a string, we make it a list
PD = ast.literal_eval(PD)

#c is the number of crossings of the diagram
c = len(PD)

#lists of potivie and negative splittings
positive_splittings = []
negative_splittings = []
for i in range(c):
    positive_splittings.append([ [PD[i][0],PD[i][1]], [PD[i][2], PD[i][3]] ])
    negative_splittings.append([ [PD[i][1], PD[i][2]], [PD[i][3], PD[i][0]] ])

#the final states correspond to elements of the list power_set
def powerset(s):
    pws = []
    x = len(s)
    for i in range(1 << x):
        pws.append([s[j] for j in range(x) if (i & (1 << j))])
    return(pws)

power_set = powerset(range(c))

#states is the list of final states, its elements are lists of 2c pairs
ps = []
ns = []
states = []
for p in power_set:
    n = [i for i in range(len(PD)) if i not in p]
    pos_pairs = [x for j in p for x in positive_splittings[j]]
    neg_pairs = [x for j in n for x in negative_splittings[j]]
    ps.append(pos_pairs)
    ns.append(neg_pairs)
    states.append(pos_pairs+neg_pairs)


#the next function counts the number of circles in a final state
def loops(L):
    loops = []
    for i in range(len(L)):
        m = L[i]
        while True:
            pairs = [x for x in L if len(set(m).intersection(x))>0]
            m = [n for p in pairs for n in p]
            if all(m.count(i) == 2 for i in m):
                break
        loops.append(m)
    return(len(set(map(tuple, loops))))

A = var('A')

#now we compute the Kauffman bracket
bracket = 0
for i in range(len(states)):
    np = len(power_set[i])
    nn = len(PD) - len(power_set[i])
    bracket = bracket + A**(np)*A**(-nn)*(-A**2-A**(-2))**(loops(states[i])-1)
bracket = simplify(bracket)

print('The Kauffman bracket is',bracket)

#next function gives the writhe of the diagram
def writhe(code):
    writhe = 0
    for c in code:
        sign = (c[1]-c[3]) % (2*len(code))
        if sign == 2*len(PD) -1:
            sign = -1
        writhe = writhe + sign
    return(writhe)

w = writhe(PD)

print('the writhe is', w)

t = var('t')

#the jones polynomial
jonesA = A**(-3*w) * bracket
jonesA = simplify(jonesA)
jones = jonesA.subs(A, t**(Rational(-.25)))

print('The Jones polynomial is',jones)
