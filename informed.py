from math import sqrt
from random import randint

def length(p1, p2):
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    return round(sqrt((x*x) + (y*y)),2)

def find(first, second, table):
    for i in range(0, len(table)):
        if (first == table[i][0] and second == table[i][1]) or (second == table[i][0] and first == table[i][1]):
            return table[i][2]
    return 10000

def low(h):
    j = 0
    for i in range(0, len(h)):
        if i == 0:
            small = h[i]
        elif h[i] < small:
            small = h[i]
            j = i
    return j

#rack = [['A', 'B', 'C', 'D', 'E'], ['F', 'G', 'H', 'I', 'J'], ['K', 'L', 'M', 'N', 'O'], ['P', 'Q', 'R', 'S', 'T'], ['U', 'V', 'W', 'X', 'Y']]

#for a in range(0, len(rack)):
#    print(rack[a])

A = [0, 0]
print("[0] - Tom Yam")
print("[1] - Beef Soup")
print("[2] - Fried Chicken")
print("[3] - Asam Pedas")
sett = input("Please enter a dish number: ")

box = []

if sett == '0':
    box.append('A')
    box.append('G')
    box.append('J')
    box.append('W')
elif sett == '1':
    box.append('A')
    box.append('J')
    box.append('M')
    box.append('Y')
elif sett == '2':
    box.append('A')
    box.append('Y')
    box.append('B')
    box.append('L')
elif sett == '3':
    box.append('A')
    box.append('G')
    box.append('H')
    box.append('M')

B = [randint(0, 4), randint(0, 4)]
C = [randint(0, 4), randint(0, 4)]
D = [randint(0, 4), randint(0, 4)]

while B[0] == A[0] or B[1] == A[1]:
    B = [randint(0, 4), randint(0, 4)]
while C[0] == A[0] or C[0] == B[0] or C[1] == A[1] or C[1] == B[1]:
    C = [randint(0, 4), randint(0, 4)]
while D[0] == A[0] or D[0] == B[0] or D[0] == C[0] or D[1] == A[1] or D[1] == B[1] or D[1] == C[1]:
    D = [randint(0, 4), randint(0, 4)]
table = [[box[0], box[1], length(A,B)], [box[0], box[2], length(A,C)], [box[0], box[3], length(A,D)], [box[1], box[2], length(B,C)], [box[1], box[3], length(B,D)], [box[2], box[3], length(C,D)]]
nodes = [box[0], box[1], box[2], box[3]]

start = nodes[randint(0,3)]
path = [start]
nodes.remove(path[len(path)-1])
iter1 =[]
pathVal = []
total = 0

print(table)
amt = 0

for j in range(0, 3):
    iter1 = []
    for i in range(0, len(nodes)):
        amt = find(path[len(path)-1], nodes[i], table)
        iter1.append(amt)
    small = low(iter1)
    #print('amt: %.2f' %amt)
    #pathVal.append(amt)
    total = total + amt
    path.append(nodes[small])
    nodes.remove(nodes[small])

#print(pathVal)
for k in range(0, len(table)):
    if (table[k][0] == start and table[k][1] == path[len(path)-1]) or (table[k][1] == start and table[k][0] == path[len(path)-1]):
        #pathVal.append(table[k][2])
        total = total + table[k][2]
path.append(start)
#print(pathVal)


print("Here are the ingredients, the basket moved along this path: %s. The basket travelled %.2fm" % (path, total))
#, (pathVal[0] + pathVal[1] + pathVal[2] + pathVal[3])