def merge (A,p,q,r):
    n1 =q-p+1
    n2= r-q
Arr= [1,2,3,4,5,6,7,8,9,10]
q=5
L=Arr[:q]
R=Arr[q:]
for i in range n1:
    L[i]=A[p+i-1]
for j =1 to n2:
    R[j] = A[q+j]
i=1
j=1
for i in range(k = p to r):
    if L[i]<=R[j]:
        A[k]=L[i]
        i= i+1
    else A[k]=R[j]
        j=j+1
    