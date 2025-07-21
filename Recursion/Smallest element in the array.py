def findMinRec(A,n):
    if n==1:
        return A[0]
    return min(A[n-1],findMinRec(A,n-1))

if __name__=="__main__":
    A=[-7,1,2,3,4,5,6,7,12]
    n=len(A)
    print(findMinRec(A,n))
