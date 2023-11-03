class Solution:
    def removeElement(self, A, elem):
        begin = 0
        for i in range(len(A)):
            if A[i] != elem:
                A[begin] = A[i]
                begin += 1
        return begin
