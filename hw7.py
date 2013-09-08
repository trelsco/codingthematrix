from mat import Mat
from vec import Vec
from cancer_data import *

from matutil import listlist2mat
from vecutil import list2vec


#from vecutil import list2vec
#from matutil import listlist2mat

## Task 1 ##
def signum(u):
    '''
    Input:
        - u: Vec
    Output:
        - v: Vec such that:
            if u[d] >= 0, then v[d] =  1
            if u[d] <  0, then v[d] = -1
    Example:
        >>> signum(Vec({1,2,3},{1:2, 2:-1})) == Vec({1,2,3},{1:1,2:-1,3:1})
        True
    '''
    v = Vec( u.D , {} )
    for entry in u.D:
        if u[entry] >= 0: v[entry] = 1
        else: v[entry] = -1
    return v

### test signum
##u = Vec({'A','B'}, {'A':3, 'B':-2})
##print(u),
##print(signum(u))
##print(signum(u) == Vec({'A', 'B'},{'A': 1, 'B': -1}))


## Task 2 ##
# In the problem description, there is mentioned a clever one-liner
# solution that is possible, without using any explicit loops or comprehension,
# hm... 
# Remembering the relationship of the dot-product and the number of
# differing elements


def fraction_wrong(A, b, w):
    '''
    Input:
        - A: a Mat with rows as feature vectors
        - b: a Vec of actual diagnoses
        - w: hypothesis Vec
    Output:
        - Fraction (as a decimal in [0,1]) of vectors incorrectly
          classified by w 
    '''
    v , frac = signum( A * w ), 0  # v becomes an row vector, frac is the number of mismatches
    for i,j in zip(v.D, b.D):
        if v[i] != b[j]: frac += 1
    return float(frac) / len(b.D)   # create percentage of mismatches to whole

#    return sum([ v[i]*w[j] for i,j in zip(v.D, b.D) if v[i] != b[j] ])*1.0 / len(b.D) 


# test fraction_wrong
##A1 = listlist2mat([[10, 7, 11, 10, 14], [1, 1, 13, 3, 2], [6, 13, 3, 2, 6], [10, 10, 12, 1, 2], [2, 1, 5, 7, 10]])
##b1 = list2vec([1,1,-1,-1,1])
##w1 = Vec(A1.D[1], {x:-2 for x in A1.D[1]})
##fraction_wrong(A1, b1, w1) == 0.6 

## Task 3 ##
## This is equivalent to the norm squared of Aw-b, ||Aw-b||^2
def loss(A, b, w):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
    Output:
        - Value of loss function at w for training data
    '''
    return ( A * w - b) * ( A * w - b)

# One reason for this choice of loss function is that the partial
# derivatives of this function  exist and are easy to compute (w/ a little bit a calculus)

## Task 4 ##
def find_grad(A, b, w):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
    Output:
        - Value of the gradient function at w
    '''
    return 2 * (A * w - b) * A

## Task 5 ##
def gradient_descent_step(A, b, w, sigma):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
        - sigma: step size
    Output:
        - The vector w' resulting from 1 iteration of gradient descent
          starting from w and moving sigma.
    '''
    return w - sigma*find_grad(A, b, w)

### test gradient_descent_step
##A1 = listlist2mat([[10, 7, 11, 10, 14], [1, 1, 13, 3, 2], [6, 13, 3, 2, 6], [10, 10, 12, 1, 2], [2, 1, 5, 7, 10]])
##b1 = list2vec([1, 1, -1, -1, 1])
##print(A1)
##print(b1)
##print(gradient_descent_step(A1, b1, Vec(A1.D[1], {x:-2 for x in A1.D[1]}), 2))
##print(gradient_descent_step(A1, b1, Vec(A1.D[1], {x:-2 for x in A1.D[1]}), 2) == Vec({0, 1, 2, 3, 4},{0: 8946, 1: 9134, 2: 11790, 3: 6866, 4: 10214}))
##

# Ungraded Task
# This is putting together all of the pieces for the lab
# into the final gradient descent procedure .



def gradient_descent(A, b, w, sigma, T):
    """
    Input:
       - A: feature matrix
       - b: diagnoses vector
       - w: hypothesis vector
       - sigma: step size
       - T: number of iterations
    Output:
       - final value of w for T iterations
    """
    _T = T  # save the initial value for T
    while T != 0:   
        w = gradient_descent_step(A, b, w, sigma)
        T -= 1    
        if _T - T == 30:   # Every 30 iterations, print diagnostic data
            print('Loss = ' + str(loss(A,b,w))),
            print('Fraction Wrong = ' + str(fraction_wrong(A,b,w)))
            _T = T
    return w





