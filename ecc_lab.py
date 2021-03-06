## Coding the Matrix: Error Correction Lab

from vec import Vec
from mat import Mat
from bitutil import noise
from GF2 import one


def listlist2mat(L):
  """Given a list of lists of field elements, return a matrix whose ith row consists
  of the elements of the ith list.  The row-labels are {0...len(L)}, and the
  column-labels are {0...len(L[0])}
  >>> A=listlist2mat([[10,20,30,40],[50,60,70,80]])
  >>> print(A)
  <BLANKLINE>
          0  1  2  3
       -------------
   0  |  10 20 30 40
   1  |  50 60 70 80
  <BLANKLINE>
"""
  m,n = len(L), len(L[0])
  return Mat((set(range(m)),set(range(n))), {(r,c):L[r][c] for r in range(m) for c in range(n)})

## Task 1 part 1
""" Create an instance of Mat representing the generator matrix G. You can use
the procedure listlist2mat in the matutil module (be sure to import first).
Since we are working over GF (2), you should use the value one from the
GF2 module to represent 1"""
# G is a 7x4 matrix, G * p = c
# where p is a four-bit message represented by a 4-vector over GF(2)
# and c is the codeword
G = listlist2mat([[ one, 0, one, one],
		  [ one, one, 0, one],
		  [   0,   0, 0, one],
		  [ one, one, one, 0],
		  [   0,   0, one, 0],
		  [   0, one,   0, 0],
		  [ one,   0,   0, 0]])


## Task 1 part 2
# Please write your answer as a list. Use one from GF2 and 0 as the elements.
encoding_1001 = None


## Task 2
# Express your answer as an instance of the Mat class.

# R is a 4x7 matrix, R * c  = p
# Which means G*(R*C) == c, and by asscociation (G*R)*c == c,
# thus G*R is the 4x4 identity matrix
R = listlist2mat([ [ 0, 0, 0, 0, 0, 0, one],
                   [ 0, 0, 0, 0, 0, one, 0],
                   [ 0, 0, 0, 0, one, 0, 0],
                   [ 0, 0, one, 0, 0, 0, 0] ])

## Task 3
# Create an instance of Mat representing the check matrix H.
H = listlist2mat([ [ 0, 0, 0, one, one, one, one] ,
                   [ 0, one, one, 0, 0, one, one] ,
                   [ one, 0, one, 0, one, 0, one] ])

## Task 4 part 1
def find_error(e):
    """
    Input: an error syndrome as an instance of Vec
    Output: the corresponding error vector e
    Examples:
        >>> find_error(Vec({0,1,2}, {0:one}))
        Vec({0, 1, 2, 3, 4, 5, 6},{3: one})
        >>> find_error(Vec({0,1,2}, {2:one}))
        Vec({0, 1, 2, 3, 4, 5, 6},{0: one})
        >>> find_error(Vec({0,1,2}, {1:one, 2:one}))
        Vec({0, 1, 2, 3, 4, 5, 6},{2: one})    
    """
    res = -1   # to store value of corrupted position; the error syndrome
    error = {0:4, 1:2, 2:1}    
    for k,v in error.items():    
      if e[k] == one: res += v   #
    if res == -1: return Vec( {i for i in range(7)}, {} )
    return Vec( {i for i in range(7)} , {res:one} )

    
## Task 4 part 2
# Use the Vec class for your answers.
non_codeword = Vec({0,1,2,3,4,5,6}, {0: one, 1:0, 2:one, 3:one, 4:0, 5:one, 6:one})
error_vector = Vec({0,1,2,3,4,5,6}, {6:one})
code_word = Vec({0,1,2,3,4,5,6}, {0: one, 1:0, 2:one, 3:one, 4:0, 5:one, 6:0})
original = Vec({0,1,2,3}, {1:one,3:one})


## Task 5
def find_error_matrix(S):
    """
    Input: a matrix S whose columns are error syndromes
    Output: a matrix whose cth column is the error corresponding to the cth column of S.
    Example:
        >>> S = listlist2mat([[0,one,one,one],[0,one,0,0],[0,0,0,one]])
        >>> find_error_matrix(S)
        Mat(({0, 1, 2, 3, 4, 5, 6}, {0, 1, 2, 3}), {(1, 2): 0, (3, 2): one, (0, 0): 0, (4, 3): one, (3, 0): 0, (6, 0): 0, (2, 1): 0, (6, 2): 0, (2, 3): 0, (5, 1): one, (4, 2): 0, (1, 0): 0, (0, 3): 0, (4, 0): 0, (0, 1): 0, (3, 3): 0, (4, 1): 0, (6, 1): 0, (3, 1): 0, (1, 1): 0, (6, 3): 0, (2, 0): 0, (5, 0): 0, (2, 2): 0, (1, 3): 0, (5, 3): 0, (5, 2): 0, (0, 2): 0})
    """
    pass

## Task 6
s = "I'm trying to free your mind, Neo. But I can only show you the door. You’re the one that has to walk through it."
P = None

## Task 7
C = None
bits_before = None
bits_after = None


## Ungraded Task
CTILDE = None

## Task 8
def correct(A):
    """
    Input: a matrix A each column of which differs from a codeword in at most one bit
    Output: a matrix whose columns are the corresponding valid codewords.
    Example:
        >>> A = Mat(({0,1,2,3,4,5,6}, {1,2,3}), {(0,3):one, (2, 1): one, (5, 2):one, (5,3):one, (0,2): one})
        >>> correct(A)
        Mat(({0, 1, 2, 3, 4, 5, 6}, {1, 2, 3}), {(0, 1): 0, (1, 2): 0, (3, 2): 0, (1, 3): 0, (3, 3): 0, (5, 2): one, (6, 1): 0, (3, 1): 0, (2, 1): 0, (0, 2): one, (6, 3): one, (4, 2): 0, (6, 2): one, (2, 3): 0, (4, 3): 0, (2, 2): 0, (5, 1): 0, (0, 3): one, (4, 1): 0, (1, 1): 0, (5, 3): one})
    """
    pass
