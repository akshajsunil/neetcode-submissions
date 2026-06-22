class Solution:
    

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        left,right=0,len(matrix[0])
        row =0
        for i in range(len(matrix)):
            if matrix[i][0]==target or matrix[i][-1]==target:
                return True
            elif target>matrix[i][0] and target < matrix[i][-1]:
                mid = (left+right)//2
         
                while left<=right:
                    if mid <0 or mid>=len(matrix[0]):
                        return False
                    mid = (left+right)//2
                    if matrix[i][mid]<target:
                        left = mid+1
                    elif matrix[i][mid]>target:
                        right = mid-1
                    else:
                        return True
                
        
        return False

        