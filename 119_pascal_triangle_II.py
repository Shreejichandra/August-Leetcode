'''Given an integer rowIndex, return the rowIndexth row of the Pascal's triangle.
Notice that the row index starts from 0.'''



class Solution:
    def getRow(self, rowIndex):
        elements_in_rows = []
        for i in range(0, rowIndex+1):
            elements_in_rows.append([])
            elements_in_rows[i].append(1)
            for j in range(1,i):
                elements_in_rows[i].append(elements_in_rows[i-1][j-1]+elements_in_rows[i-1][j])
            if i!=0:    
                elements_in_rows[i].append(1)
        
        return elements_in_rows[rowIndex]  
