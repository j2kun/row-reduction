#!/usr/bin/python

import time, random

def printMatrix(m):
   for row in m:
      print(str(row))

def rref(matrix):
   if not matrix: return

   numRows = len(matrix)
   numCols = len(matrix[0])

   i,j = 0,0
   while True:
      if i >= numRows or j >= numCols:
         break
   
      if matrix[i][j] == 0:
         nonzeroRow = i
         while nonzeroRow < numRows and matrix[nonzeroRow][j] == 0:
            nonzeroRow += 1

         if nonzeroRow == numRows:
            j += 1
            continue
         
         temp = matrix[i]
         matrix[i] = matrix[nonzeroRow]
         matrix[nonzeroRow] = temp

      pivot = matrix[i][j]
      matrix[i] = [x / pivot for x in matrix[i]] 

      for otherRow in range(0, numRows):
         if otherRow == i: 
            continue
         if matrix[otherRow][j] != 0:
            matrix[otherRow] = [y - matrix[otherRow][j]*x 
                                 for (x,y) in zip(matrix[i], matrix[otherRow])]  
      
      i += 1; j+= 1

   return matrix

B = [[random.randint(-100,100) for j in range(210)] for i in range(200)]
#printMatrix(B)

start = time.clock()
A = rref(B)
end = time.clock()
print(end - start)

#printMatrix(A)
