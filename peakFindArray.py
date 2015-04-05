__author__ = 'Carol'


def peakFindLocal(A, i, j):

    m = (i+j)/2

    if A[m-1] <= A[m] >= A[m+1]:
        return m
    elif A[m-1] > A[m]:
        return peakFindLocal(A,i,m-1)
    elif A[m] < A[m+1]:
        return peakFindLocal(A, m+1,j)


A = [1,4,6,7,13,4,2]

print A[peakFindLocal(A,0,6)]
