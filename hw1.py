from GF2 import one



## Problem 1
p1_u = [ 0, 4]
p1_v = [-1, 3]
p1_v_plus_u = [-1,7]
p1_v_minus_u = [-1,-1]
p1_three_v_minus_two_u = [-3,1]



## Problem 2
p2_u = [-1,  1, 1]
p2_v = [ 2, -1, 5]
p2_v_plus_u = [1, 0, 6]
p2_v_minus_u = [3, -2, 4]
p2_two_v_minus_u = [5,-3,9]
p2_v_plus_two_u = [0,1,7]



## Problem 3
# Write your answer using GF2's one instead of the number 1
p3_vector_sum_1 = [one,0,0]
p3_vector_sum_2 = [0,one,one]



## Problem 4
# Please express your solution as a set of the letters corresponding to the solutions.
# For example, {'a','b','c'} is the subset consisting of:
#   a (1100000), b (0110000), and c (0011000).
# Leave an empty set if it cannot be expressed in terms of the other vectors.


def addVecs(u,v):
    if not u: return v
    if not v: return u
    return [u[i] + v[i] for i in range(len(u))]

def getPowerSet(lst):
    res = [[]]
    for i in lst:
        res.extend([subset+[i] for subset in res])
    return res


def sumVecLst(lst, SuperSet):
    result = []    
    for l in lst:        
        if not result: result = SuperSet[l]        
        else:            
            for j in range(len(l)):                
                result = AddVectors(result, SuperSet[l[j]])    
    return result

S1 = {'a': [one, one, one, 0, 0, 0, 0], 'b': [0, one, one, one, 0, 0, 0],
'c': [0, 0, one, one, one, 0, 0], 'd': [0, 0, 0, one, one, one, 0],
'e': [0, 0, 0, 0, one, one, one], 'f': [0, 0, 0, 0, 0, one, one]}

P1 = getPowerSet(S1)
u1 = [0,0,one,0,0,one,0]
v1 = [0,one,0,0,0,one,0]
        
u_0010010 = {'d','c','e'}
u_0100010 = ... 



## Problem 5
# Use the same format as the previous problem

v_0010010 = {'c','d'}
v_0100010 = set()



## Problem 6
uv_a = 5 
uv_b = 6
uv_c = 16
uv_d = -1



## Problem 7
# use 'one' instead of '1'
x_gf2 = [...]



## Problem 8
v1 = [2,3,-4,1]
v2 = [1,-5,2,0]
v3 = [4,1,-1,-1]


