# -*- coding: utf-8 -*-
"""
Given an m x n integer matrix matrix, if an element is 0,
set its entire row and column to 0's, and return the matrix.

You must do it in place.


Examples:
    
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


---


Runtime: 
    
"""
import numpy as np
from itertools import chain

def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    row_lenght = matrix[0].__len__()
    np_matrix = np.array(matrix)
    
    for idx, value in enumerate(list(chain(*matrix))):
        
        x = idx % row_lenght
        y = int(idx / row_lenght)
        
        if value == 0:
            np_matrix[:, x] = 0
            np_matrix[y, :] = 0
            
            
    matrix[:] =  np.array(np_matrix).tolist()
    
    print(matrix)
    
    
matrix = [[1,1,1],[1,0,1],[1,1,1]]        
setZeroes(matrix)
    


matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]   
setZeroes(matrix)