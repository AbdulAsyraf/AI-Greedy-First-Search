from math import sqrt
from random import randint

def length(p1, p2):
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    return round(sqrt(x*x + y*y),2)

A = [0, 0]
B = [randint(0, 4), randint(0, 4)]
C = [randint(0, 4), randint(0, 4)]
D = [randint(0, 4), randint(0, 4)]
while B[0] == A[0] or B[1] == A[1]:
    B = [randint(0, 4), randint(0, 4)]

while C[0] == A[0] or C[0] == B[0] or C[1] == A[1] or C[1] == B[1]:
    C = [randint(0, 4), randint(0, 4)]

while D[0] == A[0] or D[0] == B[0] or D[0] == C[0] or D[1] == A[1] or D[1] == B[1] or D[1] == C[1]:
    D = [randint(0, 4), randint(0, 4)]

table = [['A', 'B', 'A', length(A,B)], ['A', 'C', 'A', length(A,C)], ['A', 'D', 'A', length(A,D)], ['B', 'C', 'B', length(B,C)], ['B', 'D', 'B', length(B,D)], ['C', 'D', 'C', length(C,D)]]

for i in range(0, len(table)):
    print(table[i])