class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        start=0
        end=len(matrix)-1
        cols=len(matrix[0])-1
        while(start<=end):
            mid=(start+end)//2
            if matrix[mid][0]<=target and matrix[mid][cols]>=target:
                return self.binary_search(matrix[mid][:],target)
            elif matrix[mid][0]>target:
                end=mid-1
            else:
                start=mid+1
            
        return False
    
    def binary_search(self,arr,target):
        start=0
        end=len(arr)-1
        while(start<=end):
            mid=(start+end)//2
            if arr[mid]==target:
                return True
            elif arr[mid]<target:
                start=mid+1
            else:
                end=mid-1
        return False