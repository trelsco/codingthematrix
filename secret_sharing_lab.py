
from vec import Vec
import random
from GF2 import one
from vecutil import list2vec

from independence import is_independent
from itertools import combinations

## Problem 1
def randGF2(): return random.randint(0,1)*one

a0 = list2vec([one, one,   0, one,   0, one])
b0 = list2vec([one, one,   0,   0,   0, one])

def choose_secret_vector(s,t):
    while True:
        u = list2vec([randGF2(),randGF2(),randGF2(),randGF2(),randGF2(),randGF2()])
        if a0 * u == s and b0 * u == t:
            return u
        
## Problem 2
# Give each vector as a Vec instance
def test_vecs( lst ): return all(is_independent(list(sum(v,()))) for v in combinations(lst, 3))
def gen_vec(): return list2vec( [ randGF2() for _ in range(6) ] ) 

a0, b0, a1, b1, a2, b2, a3, b3, a4, b4 = ( gen_vec() for _ in range(10) ) 

# This is a brute force method of generateing a set of secret 6-vectors
# which satisfy the condition that every set of three pairs of vectors
# are linearly independent.

while True:
    a0, b0, a1, b1, a2, b2 = ( gen_vec() for _ in range(6) )
    secret_vectors = [(a0, b0),(a1,b1),(a2,b2)]
    if test_vecs( secret_vectors ): break

while True:
    a3, b3, a4, b4 = ( gen_vec() for _ in range(4) )
    secrect_vectors  = [(a0,b0),(a3,b3),(a4,b4)]


secret_a0 = a0
secret_b0 = b0
secret_a1 = a1
secret_b1 = b1
secret_a2 = a2
secret_b2 = b2
secret_a3 = a3
secret_b3 = b3
secret_a4 = a4
secret_b4 = b4





