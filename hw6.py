# version code 988
# Please fill out this stencil and submit using the provided submission script.

from matutil import *
from GF2 import one
from vecutil import *


## Problem 1
# Write each matrix as a list of row lists

echelon_form_1 = [[1,2,0,2,0],
                  [0,1,0,3,4],
                  [0,0,2,3,4],
                  [0,0,0,2,0],
                  [0,0,0,0,4]]

echelon_form_2 = [[0,4,3,4,4],
                  [0,0,4,2,0],
                  [0,0,0,0,1],
                  [0,0,0,0,0]]

echelon_form_3 = [[1,0,0,1],
                  [0,0,0,1],
                  [0,0,0,0]]

echelon_form_4 = [[1,0,0,0],
                  [0,1,0,0],
                  [0,0,0,0],
                  [0,0,0,0]]



## Problem 2
def is_echelon(A):
    '''
    Input:
        - A: a list of row lists
    Output:
        - True if A is in echelon form
        - False otherwise
    Examples:
        >>> is_echelon([[1,1,1],[0,1,1],[0,0,1]])
        True
        >>> is_echelon([[0,1,1],[0,1,0],[0,0,1]])
        False
    '''  
    pass



## Problem 3
# Give each answer as a list

echelon_form_vec_a = [1,0,3,0]
echelon_form_vec_b = [-3,0,-2,3]
echelon_form_vec_c = [-5,0,2,0,2]



## Problem 4
# If a solution exists, give it as a list vector.
# If no solution exists, provide "None".

solving_with_echelon_form_a = None
solving_with_echelon_form_b = [21,0,2,0,0]



## Problem 5
def echelon_solve(rowlist, label_list, b):
    '''
    Input:
        - rowlist: a list of Vecs
        - label_list: a list of labels establishing an order on the domain of
                      Vecs in rowlist
        - b: a vector (represented as a list)
    Output:
        - Vec x such that rowlist * x is b
    >>> D = {'A','B','C','D','E'}
    >>> U_rows = [Vec(D, {'A':one, 'E':one}), Vec(D, {'B':one, 'E':one}), Vec(D,{'C':one})] 
    >>> b_list = [one,0,one]>>> cols = ['A', 'B', 'C', 'D', 'E']
    >>> echelon_solve(U_rows, cols, b_list)
    Vec({'B', 'C', 'A', 'D', 'E'},{'B': 0, 'C': one, 'A': one})
    '''
    D = rowlist[0].D
    v = zero_vec(D)
    for j in reversed(range(len(rowlist))):
        row = rowlist[j]        
        l = 0
        for i in label_list:
            l = i
            if(row[l] != 0):
                break
        if row[l] != 0:
            v[l] = (b[j] - v*row)/row[l]           
    return v





## Problem 6
rowlist = [Vec({'A','B','C','D'}, {'A':one, 'B':one,'D':one}), Vec({'A','B','C','D'}, {'B':one}), Vec({'A','B','C','D'},{'C':one}), Vec({'A','B','C','D'},{'D':one})]     # Provide as a list of Vec instances
label_list = ['A', 'B', 'C', 'D'] # Provide as a list
b = [one,one,0, 0]          # Provide as a list



## Problem 7
null_space_rows_a = {3,4} # Put the row numbers of M from the PDF



## Problem 8
null_space_rows_b = {4}


# give projection a try
def project_along(b,a): return ((b*a)/(a*a) if a*a !=0 else 0) *a
def project_orthogonal_1(b,a): return b - project_along(b, a)

#a = Vec({0,1,2,3},{0:-3,1:-2,2:-1,3:4})
#b = Vec({0,1,2,3},{0:7,1:2,2:5,3:0}) 
#print(project_along(b,a))

## Problem 9
# Write each vector as a list
closest_vector_1 = [1.6,3.2]
closest_vector_2 = [0,1,0]
closest_vector_3 = [3,2,1,-4]



## Problem 10
# Write each vector as a list

project_onto_1 = [2,0]
projection_orthogonal_1 = [0,1]

project_onto_2 = [-0.16666666666666666,-0.3333333333333333,0.16666666666666666]
projection_orthogonal_2 = [1.1666666666666667,1.3333333333333333,3.8333333333333335]

project_onto_3 = [1,1,4]
projection_orthogonal_3 = [0,0,0]


#a = Vec({0,1,2},{0:3,1:3,2:12})
#b = Vec({0,1,2},{0:1,1:1,2:4}) 
#print(project_along(b,a))
#print(project_orthogonal_1(b,a))


## Problem 11
norm1 = 3
norm2 = 4
norm3 = 1
